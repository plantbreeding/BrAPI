
# Group High-Dimensional Phenotypes

High-Dimensional Phenotypes description




### Get - /metabolomics [GET /brapi/v2/metabolomics{?metabolomicsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Metabolomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Metabolomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">equipment</span></td><td>object</td><td></td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.analysisType</span></td><td>string</td><td>MS or NMR. If NMR is selected, the rest of Equipment are not needed</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographyColumn</span></td><td>string</td><td>User free text to specify brand of chromotography column</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographySystem</span></td><td>string</td><td>User free text to specify brand of chromotography system</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographyType</span></td><td>string</td><td>description</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msInstrumentName</span></td><td>string</td><td>User free text to specify brand of MS system</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msInstrumentType</span></td><td>string</td><td>User free text, e.g. time of flight (TOF), triple quadropole</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msIonMode</span></td><td>string</td><td>Negative, Positive, Both</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msType</span></td><td>string</td><td>Electron Ionization (EI), Electrospray Ionization (ESI), Atmospheric Pressure Chemical Ionization (APCI), Matrix Assisted Laser Desorption Ionization (MALDI), Other (please specify below)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">headerColumns</span></td><td>array[object]</td><td>Column definitions for any matrix with this protocol</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chebi</span></td><td>string</td><td>CHEBI id; standard formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chemicalFormula</span></td><td>string</td><td>standard formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chemicalSpecies</span></td><td>object</td><td>Family of chemical</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.compoundDbId</span></td><td>string</td><td>The Unique Compound ID in this database to link to other data sets</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.inchi</span></td><td>string</td><td>InCHI is another standard universal formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.inchiKey</span></td><td>string</td><td>shortened version of inchi; users choose one or the other</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.massToCharge</span></td><td>number<br>(double)</td><td>m/z ratio, standard from output, should be a number</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.metaboliteIdentification</span></td><td>string</td><td>Name of compound</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.pubChemURL</span></td><td></td><td>The PubChem reference URL connected to this compound</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.retentionTime</span></td><td>number<br>(double)</td><td>retention time, also standard from machine output; users shoud confirm that unit is 'seconds'</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.spectraSource</span></td><td>object</td><td>The source database that defines the connection between spectra and compound</td></tr>
<tr><td>headerColumns<br>.spectraSource<br><span style="font-weight:bold;margin-left:5px">.database</span></td><td>string</td><td>Database identifier (Name or URL)</td></tr>
<tr><td>headerColumns<br>.spectraSource<br><span style="font-weight:bold;margin-left:5px">.databaseVersion</span></td><td>string</td><td>Family of chemical</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Name of compound</td></tr>
<tr><td><span style="font-weight:bold;">phenotypeUnits</span></td><td>string</td><td>Free text, e.g. relative abundance, BLUP, drBLUP, concentration (specify units, e.g. ug/g)</td></tr>
<tr><td><span style="font-weight:bold;">protocol</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.chromatography</span></td><td>string</td><td>the LC protocol, instrument settings, calibration procedure</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.massSpectrometry</span></td><td>string</td><td>instrument settings, calibration procedure</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.metaboliteIdentification</span></td><td>string</td><td>metabolite annotations were assigned to peaks</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.phenotype</span></td><td>string</td><td>BLUPs were calculated from the peak area</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.rawDataTransformation</span></td><td>string</td><td>the LCMS machine files were transformed into peak area</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sampleCollection</span></td><td>string</td><td>the tissue, time point, if the sample was frozen</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sampleExtraction</span></td><td>string</td><td>the extraction protocol used</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[string]</td><td>Relevant publication(s), DOI with details</td></tr>
</table>


 

+ Parameters
    + metabolomicsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, string) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                    "chromatographyColumn": "Waters 164 Acquity UPLC CSH Phenyl Hexyl column (1.7 IM, 1.0 x 100 mm)",
                    "chromatographySystem": "Waters Acuity UPLC",
                    "chromatographyType": "LC",
                    "msInstrumentName": "Waters Xevo G2 TOF-MS",
                    "msInstrumentType": "TOF",
                    "msIonMode": "Positive",
                    "msType": "ESI"
                },
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
                "headerColumns": [
                    {
                        "chebi": "CHEBI:75854",
                        "chemicalFormula": "C6H6O3",
                        "chemicalSpecies": "Amino Acids",
                        "compoundDbId": "LC.03.0001",
                        "inchi": "InChI=1S/C39H68O5/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-38(41)43-36-37(35-40)44-39(42)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,37,40H,3-10,15-16,21-36H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t37-/m0/s1",
                        "inchiKey": "MQGBAQLIFKSMEM-ZHARMHCNSA-N",
                        "massToCharge": 1062.5227,
                        "metaboliteIdentification": "Avenacoside A",
                        "pubChemURL": "https://pubchem.ncbi.nlm.nih.gov/compound/5988",
                        "retentionTime": 342.256063,
                        "spectraSource": {
                            "database": "gmd.mpimp-golm.mpg.de",
                            "databaseVersion": "var alk 161212"
                        },
                        "synonyms": [
                            "Avenacoside A"
                        ]
                    }
                ],
                "phenotypeUnits": "relative abundance",
                "protocol": {
                    "chromatography": "gradient of solvent A (2mM ammonium hydroxide and 0.1% formic acid) to solvent B (Acetonitrile, 0.1% formic acid)",
                    "massSpectrometry": "scanning 50-2000 m/z at 0.2 seconds per scan, alternating between MS (6 V collision energy) and MSE mode (15-30 V ramp)",
                    "metaboliteIdentification": "RAMSearch, MSFinder",
                    "phenotype": "NA",
                    "rawDataTransformation": "XCMS, centWave, RamCLUSTR",
                    "sampleCollection": "seed, mature",
                    "sampleExtraction": "biphasic, polar extract with methanol from 100 mg of tissue"
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Metabolomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">equipment</span></td><td>object</td><td></td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.analysisType</span></td><td>string</td><td>MS or NMR. If NMR is selected, the rest of Equipment are not needed</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographyColumn</span></td><td>string</td><td>User free text to specify brand of chromotography column</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographySystem</span></td><td>string</td><td>User free text to specify brand of chromotography system</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.chromatographyType</span></td><td>string</td><td>description</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msInstrumentName</span></td><td>string</td><td>User free text to specify brand of MS system</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msInstrumentType</span></td><td>string</td><td>User free text, e.g. time of flight (TOF), triple quadropole</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msIonMode</span></td><td>string</td><td>Negative, Positive, Both</td></tr>
<tr><td>equipment<br><span style="font-weight:bold;margin-left:5px">.msType</span></td><td>string</td><td>Electron Ionization (EI), Electrospray Ionization (ESI), Atmospheric Pressure Chemical Ionization (APCI), Matrix Assisted Laser Desorption Ionization (MALDI), Other (please specify below)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">headerColumns</span></td><td>array[object]</td><td>Column definitions for any matrix with this protocol</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chebi</span></td><td>string</td><td>CHEBI id; standard formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chemicalFormula</span></td><td>string</td><td>standard formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chemicalSpecies</span></td><td>object</td><td>Family of chemical</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.compoundDbId</span></td><td>string</td><td>The Unique Compound ID in this database to link to other data sets</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.inchi</span></td><td>string</td><td>InCHI is another standard universal formula</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.inchiKey</span></td><td>string</td><td>shortened version of inchi; users choose one or the other</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.massToCharge</span></td><td>number<br>(double)</td><td>m/z ratio, standard from output, should be a number</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.metaboliteIdentification</span></td><td>string</td><td>Name of compound</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.pubChemURL</span></td><td></td><td>The PubChem reference URL connected to this compound</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.retentionTime</span></td><td>number<br>(double)</td><td>retention time, also standard from machine output; users shoud confirm that unit is 'seconds'</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.spectraSource</span></td><td>object</td><td>The source database that defines the connection between spectra and compound</td></tr>
<tr><td>headerColumns<br>.spectraSource<br><span style="font-weight:bold;margin-left:5px">.database</span></td><td>string</td><td>Database identifier (Name or URL)</td></tr>
<tr><td>headerColumns<br>.spectraSource<br><span style="font-weight:bold;margin-left:5px">.databaseVersion</span></td><td>string</td><td>Family of chemical</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Name of compound</td></tr>
<tr><td><span style="font-weight:bold;">phenotypeUnits</span></td><td>string</td><td>Free text, e.g. relative abundance, BLUP, drBLUP, concentration (specify units, e.g. ug/g)</td></tr>
<tr><td><span style="font-weight:bold;">protocol</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.chromatography</span></td><td>string</td><td>the LC protocol, instrument settings, calibration procedure</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.massSpectrometry</span></td><td>string</td><td>instrument settings, calibration procedure</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.metaboliteIdentification</span></td><td>string</td><td>metabolite annotations were assigned to peaks</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.phenotype</span></td><td>string</td><td>BLUPs were calculated from the peak area</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.rawDataTransformation</span></td><td>string</td><td>the LCMS machine files were transformed into peak area</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sampleCollection</span></td><td>string</td><td>the tissue, time point, if the sample was frozen</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sampleExtraction</span></td><td>string</td><td>the extraction protocol used</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[string]</td><td>Relevant publication(s), DOI with details</td></tr>
</table>


 

+ Parameters
    + metabolomicsProtocolDbId (Required, string) ... Filter by the common crop name. Exact match.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
            "chromatographyColumn": "Waters 164 Acquity UPLC CSH Phenyl Hexyl column (1.7 IM, 1.0 x 100 mm)",
            "chromatographySystem": "Waters Acuity UPLC",
            "chromatographyType": "LC",
            "msInstrumentName": "Waters Xevo G2 TOF-MS",
            "msInstrumentType": "TOF",
            "msIonMode": "Positive",
            "msType": "ESI"
        },
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
        "headerColumns": [
            {
                "chebi": "CHEBI:75854",
                "chemicalFormula": "C6H6O3",
                "chemicalSpecies": "Amino Acids",
                "compoundDbId": "LC.03.0001",
                "inchi": "InChI=1S/C39H68O5/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-38(41)43-36-37(35-40)44-39(42)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,37,40H,3-10,15-16,21-36H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t37-/m0/s1",
                "inchiKey": "MQGBAQLIFKSMEM-ZHARMHCNSA-N",
                "massToCharge": 1062.5227,
                "metaboliteIdentification": "Avenacoside A",
                "pubChemURL": "https://pubchem.ncbi.nlm.nih.gov/compound/5988",
                "retentionTime": 342.256063,
                "spectraSource": {
                    "database": "gmd.mpimp-golm.mpg.de",
                    "databaseVersion": "var alk 161212"
                },
                "synonyms": [
                    "Avenacoside A"
                ]
            }
        ],
        "phenotypeUnits": "relative abundance",
        "protocol": {
            "chromatography": "gradient of solvent A (2mM ammonium hydroxide and 0.1% formic acid) to solvent B (Acetonitrile, 0.1% formic acid)",
            "massSpectrometry": "scanning 50-2000 m/z at 0.2 seconds per scan, alternating between MS (6 V collision energy) and MSE mode (15-30 V ramp)",
            "metaboliteIdentification": "RAMSearch, MSFinder",
            "phenotype": "NA",
            "rawDataTransformation": "XCMS, centWave, RamCLUSTR",
            "sampleCollection": "seed, mature",
            "sampleExtraction": "biphasic, polar extract with methanol from 100 mg of tissue"
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">tissue_type</span></td><td>string</td><td>description</td></tr>
</table>


 

+ Parameters
    + metabolomicsProtocolDbId (Required, string) ... Path parameter protocol id
    + studyDbId (Optional, string) ... filter by study
    + observationUnitDbId (Optional, string) ... filter by study
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the NIRS Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">deviceType</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">header_column_names</span></td><td>array[integer]</td><td>description</td></tr>
</table>


 

+ Parameters
    + nirsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, string) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the NIRS Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">deviceType</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">header_column_names</span></td><td>array[integer]</td><td>description</td></tr>
</table>


 

+ Parameters
    + nirsProtocolDbId (Required, string) ... Filter by the common crop name. Exact match.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">tissue_type</span></td><td>string</td><td>description</td></tr>
</table>


 

+ Parameters
    + nirsProtocolDbId (Required, string) ... Path parameter protocol id
    + studyDbId (Optional, string) ... filter by study
    + observationUnitDbId (Optional, string) ... filter by study
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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




### Get - /transcriptomics [GET /brapi/v2/transcriptomics{?transcriptomicsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Transcriptomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">headerColumns</span></td><td>array[object]</td><td>Column definitions for any matrix with this protocol</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chromosome</span></td><td>string</td><td>The chromosome of interest</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.functionalAnnotation</span></td><td>string</td><td>functional annotation</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.geneId</span></td><td>string</td><td>ID of a functional gene</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.positionLeft</span></td><td>integer</td><td>Position to the left</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.positionRight</span></td><td>integer</td><td>Position to the right</td></tr>
<tr><td><span style="font-weight:bold;">protocol</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.annotationFile</span></td><td>string</td><td>The reference annotation file used</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.countingSoftware</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareDescription</span></td><td>string</td><td>The description of a piece of software</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareName</span></td><td>string</td><td>Human readable name for a piece of software</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareURL</span></td><td>string</td><td>A URL where the software can be accessed/downloaded</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareVersion</span></td><td>string</td><td>The version of a piece of software</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.instrumentModel</span></td><td>string</td><td>The specific equipment used to perform sequencing</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.layout</span></td><td>string</td><td>layout (single vs. paired end reads)</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.libraryComments</span></td><td>string</td><td>libraryComments</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.libraryMethod</span></td><td>string</td><td>libraryMethod</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.mappingSoftware</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareDescription</span></td><td>string</td><td>The description of a piece of software</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareName</span></td><td>string</td><td>Human readable name for a piece of software</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareURL</span></td><td>string</td><td>A URL where the software can be accessed/downloaded</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareVersion</span></td><td>string</td><td>The version of a piece of software</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.nucleicAcidExtractionMethod</span></td><td>string</td><td>How DNA/RNA was extracted (Hot borate, Qiagen kit, etc)</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.referenceGenome</span></td><td>object</td><td>Reference genome used for sequencing alignment</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeAssemblyName</span></td><td>string</td><td>The human readable name of the reference genome</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeURL</span></td><td>string</td><td>A URL pointing to the location of the reference genome file. (example file types; .fasta, .fa, etc)</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeVersion</span></td><td>string</td><td>the version number of the reference genome</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingCenter</span></td><td>string</td><td>The organization where sequencing occured</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingLength</span></td><td>integer</td><td>The sequence length in nucleotides</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingPlatform</span></td><td>string</td><td>The system used to perform sequencing</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units describing the data in this matrix (counts, FPKM, etc)</td></tr>
</table>


 

+ Parameters
    + transcriptomicsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, string) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "headerColumns": [
                    {
                        "chromosome": "B73V4_ctg150",
                        "functionalAnnotation": "polyphenol oxidase1",
                        "geneId": "ZeamMp004",
                        "positionLeft": 48820,
                        "positionRight": 51164
                    }
                ],
                "protocol": {
                    "annotationFile": "annotationFile",
                    "countingSoftware": {
                        "softwareDescription": "Maps and counts transcriptomics data",
                        "softwareName": "DNA Mappy County",
                        "softwareURL": "https://example.com/downloads/DNA_Mappy_County/1.2",
                        "softwareVersion": "1.2"
                    },
                    "instrumentModel": "NextSeq 500",
                    "layout": "single",
                    "libraryComments": "We used the 3'RNA-seq method",
                    "libraryMethod": "3'RNA-seq",
                    "mappingSoftware": {
                        "softwareDescription": "Maps and counts transcriptomics data",
                        "softwareName": "DNA Mappy County",
                        "softwareURL": "https://example.com/downloads/DNA_Mappy_County/1.2",
                        "softwareVersion": "1.2"
                    },
                    "nucleicAcidExtractionMethod": "Hot borate",
                    "referenceGenome": {
                        "genomeAssemblyName": "Zm-B73-REFERENCE-NAM-5.0",
                        "genomeURL": "https://www.maizegdb.org/genome/assembly/Zm-B73-REFERENCE-NAM-5.0",
                        "genomeVersion": "5.0"
                    },
                    "sequencingCenter": "Cornell University Institute of Biotechnology",
                    "sequencingLength": 86,
                    "sequencingPlatform": "Illumina",
                    "units": "counts"
                },
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




### Get - /transcriptomics/{transcriptomicsProtocolDbId} [GET /brapi/v2/transcriptomics/{transcriptomicsProtocolDbId}]

Get a single Transcriptomics Protocol by Id. This can be used to quickly get the details of a TranscriptomicsProtocol when you have the Id from another entity.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">headerColumns</span></td><td>array[object]</td><td>Column definitions for any matrix with this protocol</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.chromosome</span></td><td>string</td><td>The chromosome of interest</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.functionalAnnotation</span></td><td>string</td><td>functional annotation</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.geneId</span></td><td>string</td><td>ID of a functional gene</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.positionLeft</span></td><td>integer</td><td>Position to the left</td></tr>
<tr><td>headerColumns<br><span style="font-weight:bold;margin-left:5px">.positionRight</span></td><td>integer</td><td>Position to the right</td></tr>
<tr><td><span style="font-weight:bold;">protocol</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.annotationFile</span></td><td>string</td><td>The reference annotation file used</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.countingSoftware</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareDescription</span></td><td>string</td><td>The description of a piece of software</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareName</span></td><td>string</td><td>Human readable name for a piece of software</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareURL</span></td><td>string</td><td>A URL where the software can be accessed/downloaded</td></tr>
<tr><td>protocol<br>.countingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareVersion</span></td><td>string</td><td>The version of a piece of software</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.instrumentModel</span></td><td>string</td><td>The specific equipment used to perform sequencing</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.layout</span></td><td>string</td><td>layout (single vs. paired end reads)</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.libraryComments</span></td><td>string</td><td>libraryComments</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.libraryMethod</span></td><td>string</td><td>libraryMethod</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.mappingSoftware</span></td><td>object</td><td></td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareDescription</span></td><td>string</td><td>The description of a piece of software</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareName</span></td><td>string</td><td>Human readable name for a piece of software</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareURL</span></td><td>string</td><td>A URL where the software can be accessed/downloaded</td></tr>
<tr><td>protocol<br>.mappingSoftware<br><span style="font-weight:bold;margin-left:5px">.softwareVersion</span></td><td>string</td><td>The version of a piece of software</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.nucleicAcidExtractionMethod</span></td><td>string</td><td>How DNA/RNA was extracted (Hot borate, Qiagen kit, etc)</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.referenceGenome</span></td><td>object</td><td>Reference genome used for sequencing alignment</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeAssemblyName</span></td><td>string</td><td>The human readable name of the reference genome</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeURL</span></td><td>string</td><td>A URL pointing to the location of the reference genome file. (example file types; .fasta, .fa, etc)</td></tr>
<tr><td>protocol<br>.referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeVersion</span></td><td>string</td><td>the version number of the reference genome</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingCenter</span></td><td>string</td><td>The organization where sequencing occured</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingLength</span></td><td>integer</td><td>The sequence length in nucleotides</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.sequencingPlatform</span></td><td>string</td><td>The system used to perform sequencing</td></tr>
<tr><td>protocol<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units describing the data in this matrix (counts, FPKM, etc)</td></tr>
</table>


 

+ Parameters
    + transcriptomicsProtocolDbId (Required, string) ... Filter by the common crop name. Exact match.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "headerColumns": [
            {
                "chromosome": "B73V4_ctg150",
                "functionalAnnotation": "polyphenol oxidase1",
                "geneId": "ZeamMp004",
                "positionLeft": 48820,
                "positionRight": 51164
            }
        ],
        "protocol": {
            "annotationFile": "annotationFile",
            "countingSoftware": {
                "softwareDescription": "Maps and counts transcriptomics data",
                "softwareName": "DNA Mappy County",
                "softwareURL": "https://example.com/downloads/DNA_Mappy_County/1.2",
                "softwareVersion": "1.2"
            },
            "instrumentModel": "NextSeq 500",
            "layout": "single",
            "libraryComments": "We used the 3'RNA-seq method",
            "libraryMethod": "3'RNA-seq",
            "mappingSoftware": {
                "softwareDescription": "Maps and counts transcriptomics data",
                "softwareName": "DNA Mappy County",
                "softwareURL": "https://example.com/downloads/DNA_Mappy_County/1.2",
                "softwareVersion": "1.2"
            },
            "nucleicAcidExtractionMethod": "Hot borate",
            "referenceGenome": {
                "genomeAssemblyName": "Zm-B73-REFERENCE-NAM-5.0",
                "genomeURL": "https://www.maizegdb.org/genome/assembly/Zm-B73-REFERENCE-NAM-5.0",
                "genomeVersion": "5.0"
            },
            "sequencingCenter": "Cornell University Institute of Biotechnology",
            "sequencingLength": 86,
            "sequencingPlatform": "Illumina",
            "units": "counts"
        },
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




### Get - /transcriptomics/{transcriptomicsProtocolDbId}/matrix [GET /brapi/v2/transcriptomics/{transcriptomicsProtocolDbId}/matrix{?studyDbId}{?observationUnitDbId}]

Get a Transcriptomics data matrix by TranscriptomicsProtocolDbId



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">tissue_type</span></td><td>string</td><td>description</td></tr>
</table>


 

+ Parameters
    + transcriptomicsProtocolDbId (Required, string) ... Path parameter protocol id
    + studyDbId (Optional, string) ... filter by study
    + observationUnitDbId (Optional, string) ... filter by study
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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

