
# Group High-Dimensional Phenotypes

High-Dimensional Phenotypes description




### Get - /metabolomics/instances [GET /brapi/v2/metabolomics/instances{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Metabolomics Instances



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.charge</span></td><td>string</td><td>Positive or Negative charge associated with metabolite, can be derived from mass to charge ratio</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chebi</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chemicalFormula</span></td><td>string</td><td>metaboltie chemical formula</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.fragmentation</span></td><td>string</td><td>Fragmentation m/z intensity output</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.inchi</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, another standard formula</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.inchiKey</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, shortened version of InCHI ID</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.massToCharge</span></td><td>number<br>(double)</td><td>m/z ratio, standard from output, should be a number</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteId</span></td><td>string</td><td>metabolite ID in metabolite data file; these are entered as columns in this file in Metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteReliability</span></td><td>integer</td><td>A number 1 through 5, related to Schymanski et al 2014, doi.org/10.1021/es5002105. 1= confrimed structure, 2= probable structure, 3= tentative candidate, 4=unequivocal molecular formula, 5=exact mass of interest</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteSearchEngineScore</span></td><td>string</td><td>Score provided by search engine</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteSpecies</span></td><td>string</td><td>Metabolite categorization, autofilled in Metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.modifications</span></td><td>string</td><td>List metabolite modifications prior to instrument analysis</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.pubChemId</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, pubchem URL is another standard</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.putativeMetaboliteIdentification</span></td><td>string</td><td>Naming this putative anntoation because untargeted data, not same curation process as metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.putativeMetaboliteIndentificationSynonyms</span></td><td>string</td><td>metabolite synonyms, alternate names of any of the above</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.retentionTime</span></td><td>number<br>(double)</td><td>retention time, also standard from machine output; users should confirm that unit is 'seconds'</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteDatabase</span></td><td>string</td><td>Database used for metabolic review, and sample upload</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteDatabaseVersion</span></td><td>string</td><td>Version of database used for metabolic review, and sample upload</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Metabolomics protocol</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a Metabolomics Instance
    + protocolDbId (Optional, string) ... A unique identifier for a Metabolomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "columnHeaders": [
                    {
                        "charge": "positive",
                        "chebi": "CHEBI:75854",
                        "chemicalFormula": "C6H6O3",
                        "fragmentation": "239:3349 240:1454 342:3557 343:1562",
                        "inchi": "InChI=1S/C39H68O5/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-38(41)43-36-37(35-40)44-39(42)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,37,40H,3-10,15-16,21-36H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t37-/m0/s1",
                        "inchiKey": "MQGBAQLIFKSMEM-ZHARMHCNSA-N",
                        "massToCharge": 1062.5227,
                        "metaboliteId": "1,2,4-Benzenetriol",
                        "metaboliteReliability": 1,
                        "metaboliteSearchEngineScore": "?",
                        "metaboliteSpecies": "Amino Acids",
                        "modifications": "trimethylsilation",
                        "pubChemId": "10787",
                        "putativeMetaboliteIdentification": "Phenylalanine, sucrose, avenanthramide",
                        "putativeMetaboliteIndentificationSynonyms": "L-Phenylalanine, sugar, caffeoyltyramine",
                        "retentionTime": 342.256063
                    }
                ],
                "instanceId": "abc123",
                "metaboliteDatabase": "gmd.mpimp-golm.mpg.de",
                "metaboliteDatabaseVersion": "var5 alk 161212",
                "protocolDbId": "f60f15b2",
                "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /metabolomics/matrix [GET /brapi/v2/metabolomics/matrix{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?page}{?pageSize}]

Get a matrix of Metabolomics data. A valid request must include a "protocolDbId", an "instanceDbId", or both.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Any comments collected by the researcher during sample preparation and data collection</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>Identifier containing the unique observation unit linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.plantAge</span></td><td>integer</td><td>Sample plant's age; numerical representation of days after planting</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.sampleDbId</span></td><td>string</td><td>Identifier containing the unique sample name linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.specimenSource</span></td><td>string</td><td>Description of specimen source</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueCollectionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for tissue collection</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueDevStage</span></td><td>string</td><td>Stage in life of the plant structure during which the sample was taken, in the form of an accession number from Plant Ontology</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueStorage</span></td><td>string</td><td>Where tissue is stored</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>Description of the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number from Plant Ontology</td></tr>
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.charge</span></td><td>string</td><td>Positive or Negative charge associated with metabolite, can be derived from mass to charge ratio</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chebi</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chemicalFormula</span></td><td>string</td><td>metaboltie chemical formula</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.fragmentation</span></td><td>string</td><td>Fragmentation m/z intensity output</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.inchi</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, another standard formula</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.inchiKey</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, shortened version of InCHI ID</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.massToCharge</span></td><td>number<br>(double)</td><td>m/z ratio, standard from output, should be a number</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteId</span></td><td>string</td><td>metabolite ID in metabolite data file; these are entered as columns in this file in Metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteReliability</span></td><td>integer</td><td>A number 1 through 5, related to Schymanski et al 2014, doi.org/10.1021/es5002105. 1= confrimed structure, 2= probable structure, 3= tentative candidate, 4=unequivocal molecular formula, 5=exact mass of interest</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteSearchEngineScore</span></td><td>string</td><td>Score provided by search engine</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.metaboliteSpecies</span></td><td>string</td><td>Metabolite categorization, autofilled in Metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.modifications</span></td><td>string</td><td>List metabolite modifications prior to instrument analysis</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.pubChemId</span></td><td>string</td><td>at least one cmpdID required; all can be generated from CHEBI and/or InChI, pubchem URL is another standard</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.putativeMetaboliteIdentification</span></td><td>string</td><td>Naming this putative anntoation because untargeted data, not same curation process as metabolights</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.putativeMetaboliteIndentificationSynonyms</span></td><td>string</td><td>metabolite synonyms, alternate names of any of the above</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.retentionTime</span></td><td>number<br>(double)</td><td>retention time, also standard from machine output; users should confirm that unit is 'seconds'</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteDatabase</span></td><td>string</td><td>Database used for metabolic review, and sample upload</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteDatabaseVersion</span></td><td>string</td><td>Version of database used for metabolic review, and sample upload</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Metabolomics protocol</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a Metabolomics Instance
    + protocolDbId (Optional, string) ... A unique identifier for a Metabolomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
        "columnHeaders": [
            {
                "charge": "positive",
                "chebi": "CHEBI:75854",
                "chemicalFormula": "C6H6O3",
                "fragmentation": "239:3349 240:1454 342:3557 343:1562",
                "inchi": "InChI=1S/C39H68O5/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-38(41)43-36-37(35-40)44-39(42)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,37,40H,3-10,15-16,21-36H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t37-/m0/s1",
                "inchiKey": "MQGBAQLIFKSMEM-ZHARMHCNSA-N",
                "massToCharge": 1062.5227,
                "metaboliteId": "1,2,4-Benzenetriol",
                "metaboliteReliability": 1,
                "metaboliteSearchEngineScore": "?",
                "metaboliteSpecies": "Amino Acids",
                "modifications": "trimethylsilation",
                "pubChemId": "10787",
                "putativeMetaboliteIdentification": "Phenylalanine, sucrose, avenanthramide",
                "putativeMetaboliteIndentificationSynonyms": "L-Phenylalanine, sugar, caffeoyltyramine",
                "retentionTime": 342.256063
            }
        ],
        "data": [
            {
                "comments": "root",
                "observationUnitDbId": "e3675c4a",
                "plantAge": 20,
                "row": [
                    "0.0355",
                    "0.1442",
                    "0.4322",
                    "0.5473"
                ],
                "sampleDbId": "BB251_101",
                "specimenSource": "USDA_GRIN_2020",
                "tissueCollectionTimestamp": "2024-01-02 03:04:05",
                "tissueDevStage": "PO:0001083, inflorescence development stage",
                "tissueStorage": "-80 degrees",
                "tissueType": "PO:0009010; seed"
            }
        ],
        "instanceId": "abc123",
        "metaboliteDatabase": "gmd.mpimp-golm.mpg.de",
        "metaboliteDatabaseVersion": "var5 alk 161212",
        "protocolDbId": "f60f15b2",
        "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /metabolomics/protocols [GET /brapi/v2/metabolomics/protocols{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Metabolomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Metabolomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">analysisType</span></td><td>string</td><td>Mass spectrometry or Nuclear Magnetic Resonance Spectroscopy</td></tr>
<tr><td><span style="font-weight:bold;">chromatography</span></td><td>object</td><td></td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyAutoSamplerModel</span></td><td>string</td><td>Name of autosampler</td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyColumnModel</span></td><td>string</td><td>Brand of chromotography column</td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyColumnType</span></td><td>string</td><td>the type of chromotography column</td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyInstrument</span></td><td>string</td><td>Brand of chromotography system</td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyProtocol</span></td><td>string</td><td>the LC protocol, instrument settings, calibration procedure</td></tr>
<tr><td>chromatography<br><span style="font-weight:bold;margin-left:5px">.chromatographyType</span></td><td>string</td><td>Type of chromatography used, liquid or gas</td></tr>
<tr><td><span style="font-weight:bold;">comments</span></td><td>string</td><td>Any comments collected by the researcher about protocols, machinery, etc. corresponding to a sample</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">massSpectrometry</span></td><td>object</td><td></td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryInstrument</span></td><td>string</td><td>Brand and model of MS system</td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryIonSource</span></td><td>string</td><td>Ion Source used by mass analyzer. Electron Ionization (EI), Electrospray Ionization (ESI), Atmospheric Pressure Chemical Ionization (APCI), Matrix Assisted Laser Desorption Ionization (MALDI), Other (please specify below)</td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryMassAnalyzer</span></td><td>string</td><td>Mass analyzer used for mass-to-charge ratio</td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryProtocol</span></td><td>string</td><td>Mass spectrometry protocol, instrument settings, calibration procedure, or link to protocol</td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryScanMZRange</span></td><td>number</td><td>single vs paired end (60-800)</td></tr>
<tr><td>massSpectrometry<br><span style="font-weight:bold;margin-left:5px">.massSpectrometryScanPolarity</span></td><td>string</td><td>Negative, Positive, Both</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteAnnotationMethod</span></td><td>string</td><td>metabolite annotations were assigned to peaks</td></tr>
<tr><td><span style="font-weight:bold;">metaboliteSearchEngine</span></td><td>string</td><td>How the metabolite database was searched</td></tr>
<tr><td><span style="font-weight:bold;">protocolDescription</span></td><td>string</td><td>Human-readable text describing the protocol in more detail</td></tr>
<tr><td><span style="font-weight:bold;">protocolTitle</span></td><td>string</td><td>Human-readable string summarizing the protocol</td></tr>
<tr><td><span style="font-weight:bold;">rawDataTransformationProtocol</span></td><td>string</td><td>Methods for how files from the LCMS machine were transformed into peak area</td></tr>
<tr><td><span style="font-weight:bold;">sampleExtractionMethod</span></td><td>string</td><td>the Sample extraction method used</td></tr>
</table>


 

+ Parameters
    + protocolDbId (Optional, string) ... A unique identifier for a Metabolomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "analysisType": "MS",
                "chromatography": {
                    "chromatographyAutoSamplerModel": "Waters Autosampler",
                    "chromatographyColumnModel": "Waters 164 Acquity UPLC CSH Phenyl Hexyl column (1.7 IM, 1.0 x 100 mm)",
                    "chromatographyColumnType": "Phenyl Hexyl column",
                    "chromatographyInstrument": "Waters Acuity UPLC",
                    "chromatographyProtocol": "gradient of solvent A (2mM ammonium hydroxide and 0.1% formic acid) to solvent B (Acetonitrile, 0.1% formic acid)",
                    "chromatographyType": "LC"
                },
                "comments": "comments",
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
                "massSpectrometry": {
                    "massSpectrometryInstrument": "Waters Xevo G2 TOF-MS",
                    "massSpectrometryIonSource": "ESI",
                    "massSpectrometryMassAnalyzer": "TOF",
                    "massSpectrometryProtocol": "scanning 50-2000 m/z at 0.2 seconds per scan, alternating between MS (6 V collision energy) and MSE mode (15-30 V ramp)",
                    "massSpectrometryScanMZRange": 60,
                    "massSpectrometryScanPolarity": "Positive"
                },
                "metaboliteAnnotationMethod": "Freetext or URL method",
                "metaboliteSearchEngine": "TagFinder4.1 manual supervised annotation",
                "protocolDbId": "f60f15b2",
                "protocolDescription": "Details on sample preparation, calibration, & model used",
                "protocolTitle": "Foss DS3 NIRS protocol for ground butter beans",
                "rawDataTransformationProtocol": "XCMS, centWave, RamCLUSTR",
                "sampleExtractionMethod": "Liquid-Liquid Extraction"
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




### Get - /nirs/instances [GET /brapi/v2/nirs/instances{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of NIRS Instances



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.frequency</span></td><td>integer</td><td>Wavelength in nanometers</td></tr>
<tr><td><span style="font-weight:bold;">deviceSerialNumber</span></td><td>string</td><td>Serial number of the spectrometer device</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the NIRS protocol</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a NIRS Instance
    + protocolDbId (Optional, string) ... A unique identifier for a NIRS Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "columnHeaders": [
                    {
                        "frequency": 740
                    },
                    {
                        "frequency": 742
                    },
                    {
                        "frequency": 744
                    },
                    {
                        "frequency": 746
                    }
                ],
                "deviceSerialNumber": "ABC1234567",
                "instanceId": "abc123",
                "protocolDbId": "f60f15b2",
                "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /nirs/matrix [GET /brapi/v2/nirs/matrix{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?page}{?pageSize}]

Get a matrix of NIRS data. A valid request must include a "protocolDbId", an "instanceDbId", or both.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Any comments collected by the researcher during sample preparation and data collection, specific to each scan.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>Identifier containing the unique observation unit linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.sampleDbId</span></td><td>string</td><td>Identifier containing the unique sample name linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.scanTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp specific to each individual scan, provided by some spectrometers.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>Description of the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number from Plant Ontology</td></tr>
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.frequency</span></td><td>integer</td><td>Wavelength in nanometers</td></tr>
<tr><td><span style="font-weight:bold;">deviceSerialNumber</span></td><td>string</td><td>Serial number of the spectrometer device</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the NIRS protocol</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a NIRS Instance
    + protocolDbId (Optional, string) ... A unique identifier for a NIRS Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
        "columnHeaders": [
            {
                "frequency": 740
            },
            {
                "frequency": 742
            },
            {
                "frequency": 744
            },
            {
                "frequency": 746
            }
        ],
        "data": [
            {
                "comments": "root",
                "observationUnitDbId": "e3675c4a",
                "row": [
                    "0.0355",
                    "0.1442",
                    "0.4322",
                    "0.5473"
                ],
                "sampleDbId": "BB251_101",
                "scanTimestamp": "2024-01-02 03:04:05",
                "tissueType": "PO:0009010; seed"
            }
        ],
        "deviceSerialNumber": "ABC1234567",
        "instanceId": "abc123",
        "protocolDbId": "f60f15b2",
        "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /nirs/protocols [GET /brapi/v2/nirs/protocols{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of NIRS Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the NIRS Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">deviceFrequencyNumber</span></td><td>integer</td><td>Total number of wavelengths measured in each scan of the device</td></tr>
<tr><td><span style="font-weight:bold;">deviceType</span></td><td>string</td><td>Spectrometer device name</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>Link to detailed Standard Operating Procedure (SOP) for protocol</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">protocolDescription</span></td><td>string</td><td>Human-readable text describing the protocol in more detail</td></tr>
<tr><td><span style="font-weight:bold;">protocolTitle</span></td><td>string</td><td>Human-readable string summarizing the protocol</td></tr>
</table>


 

+ Parameters
    + protocolDbId (Optional, string) ... A unique identifier for a NIRS Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "deviceFrequencyNumber": 200,
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
                "protocolDbId": "f60f15b2",
                "protocolDescription": "Details on sample preparation, calibration, & model used",
                "protocolTitle": "Foss DS3 NIRS protocol for ground butter beans"
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




### Get - /transcriptomics/instances [GET /brapi/v2/transcriptomics/instances{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Transcriptomics Instances



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chromosome</span></td><td>string</td><td>The chromosome of interest</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.functionalAnnotation</span></td><td>string</td><td>functional annotation</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.geneId</span></td><td>string</td><td>ID of a functional gene</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.positionLeft</span></td><td>integer</td><td>Position to the left</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.positionRight</span></td><td>integer</td><td>Position to the right</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics protocol</td></tr>
<tr><td><span style="font-weight:bold;">researchPurpose</span></td><td>string</td><td>Human-readable string summarizing the research purpose</td></tr>
<tr><td><span style="font-weight:bold;">sraAccession</span></td><td>string</td><td>Accession name provided upon SRA upload</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a Transcriptomics Instance
    + protocolDbId (Optional, string) ... A unique identifier for a Transcriptomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "columnHeaders": [
                    {
                        "chromosome": "B73V4_ctg150",
                        "functionalAnnotation": "polyphenol oxidase1",
                        "geneId": "ZeamMp004",
                        "positionLeft": 48820,
                        "positionRight": 51164
                    }
                ],
                "instanceId": "abc123",
                "protocolDbId": "f60f15b2",
                "researchPurpose": "Yield Trial Summer 2025",
                "sraAccession": "ABC1234567",
                "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /transcriptomics/matrix [GET /brapi/v2/transcriptomics/matrix{?instanceDbId}{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?page}{?pageSize}]

Get a matrix of Transcriptomics data. A valid request must include a "protocolDbId", an "instanceDbId", or both.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Any comments collected by the researcher during sample preparation and data collection, specific to each scan.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>Identifier containing the unique observation unit linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>array[string]</td><td>description</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.sampleDbId</span></td><td>string</td><td>Identifier containing the unique sample name linked to an experiment ID</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueDevStage</span></td><td>string</td><td>Stage in life of the plant structure during which the sample was taken, in the form of an accession number from Plant Ontology</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueHarvestDate</span></td><td>string<br>(date-time)</td><td>Date of tissue harvest</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueHarvester</span></td><td>string</td><td>Identifier for the researcher who harvested the tissue</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>Description of the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number from Plant Ontology</td></tr>
<tr><td><span style="font-weight:bold;">columnHeaders</span></td><td>array[object]</td><td>An ordered list of column header definitions for this instance</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.chromosome</span></td><td>string</td><td>The chromosome of interest</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.functionalAnnotation</span></td><td>string</td><td>functional annotation</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.geneId</span></td><td>string</td><td>ID of a functional gene</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.positionLeft</span></td><td>integer</td><td>Position to the left</td></tr>
<tr><td>columnHeaders<br><span style="font-weight:bold;margin-left:5px">.positionRight</span></td><td>integer</td><td>Position to the right</td></tr>
<tr><td><span style="font-weight:bold;">instanceId</span></td><td>string</td><td>Relates data matrix to a specific instance</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics protocol</td></tr>
<tr><td><span style="font-weight:bold;">researchPurpose</span></td><td>string</td><td>Human-readable string summarizing the research purpose</td></tr>
<tr><td><span style="font-weight:bold;">sraAccession</span></td><td>string</td><td>Accession name provided upon SRA upload</td></tr>
<tr><td><span style="font-weight:bold;">uploadTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp for initial upload of spectral data matrix into database</td></tr>
</table>


 

+ Parameters
    + instanceDbId (Optional, string) ... A unique identifier for a Transcriptomics Instance
    + protocolDbId (Optional, string) ... A unique identifier for a Transcriptomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
        "columnHeaders": [
            {
                "chromosome": "B73V4_ctg150",
                "functionalAnnotation": "polyphenol oxidase1",
                "geneId": "ZeamMp004",
                "positionLeft": 48820,
                "positionRight": 51164
            }
        ],
        "data": [
            {
                "comments": "Senescing tissue",
                "observationUnitDbId": "e3675c4a",
                "row": [
                    "0.0355",
                    "0.1442",
                    "0.4322",
                    "0.5473"
                ],
                "sampleDbId": "BB251_101",
                "tissueDevStage": "PO:0001083, inflorescence development stage",
                "tissueHarvestDate": "2024-01-02 03:04:05",
                "tissueHarvester": "MLWilson",
                "tissueType": "PO:0009010; seed"
            }
        ],
        "instanceId": "abc123",
        "protocolDbId": "f60f15b2",
        "researchPurpose": "Yield Trial Summer 2025",
        "sraAccession": "ABC1234567",
        "uploadTimestamp": "2024-01-03 03:04:05"
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




### Get - /transcriptomics/protocols [GET /brapi/v2/transcriptomics/protocols{?protocolDbId}{?observationUnitDbId}{?sampleDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Transcriptomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">annotationFile</span></td><td>object</td><td>The reference annotation file used</td></tr>
<tr><td>annotationFile<br><span style="font-weight:bold;margin-left:5px">.annotationFileName</span></td><td>string</td><td>The human readable name of the annotation file</td></tr>
<tr><td>annotationFile<br><span style="font-weight:bold;margin-left:5px">.annotationFileURL</span></td><td>string</td><td>A URL pointing to the location of the annotation file. (example file types; .gff, .gff3, .gtf, etc)</td></tr>
<tr><td>annotationFile<br><span style="font-weight:bold;margin-left:5px">.annotationFileVersion</span></td><td>string</td><td>the version of the annotation file</td></tr>
<tr><td><span style="font-weight:bold;">countingSoftware</span></td><td>string</td><td>Counting software used to quantify gene expression levels based on mapped reads</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">instrumentModel</span></td><td>string</td><td>The specific equipment used to perform sequencing</td></tr>
<tr><td><span style="font-weight:bold;">layout</span></td><td>string</td><td>layout (single vs. paired end reads)</td></tr>
<tr><td><span style="font-weight:bold;">libraryComments</span></td><td>string</td><td>libraryComments</td></tr>
<tr><td><span style="font-weight:bold;">libraryMethod</span></td><td>string</td><td>Technique used to prepare the library</td></tr>
<tr><td><span style="font-weight:bold;">mappingSoftware</span></td><td>string</td><td>Mapping software used to align reads to a reference genome or transcriptome</td></tr>
<tr><td><span style="font-weight:bold;">nucleicAcidExtractionMethod</span></td><td>string</td><td>Kit and or method used for nucleic acid extraction (Hot borate, Qiagen kit, etc)</td></tr>
<tr><td><span style="font-weight:bold;">protocolDescription</span></td><td>string</td><td>Human-readable text describing the protocol in more detail</td></tr>
<tr><td><span style="font-weight:bold;">protocolTitle</span></td><td>string</td><td>Human-readable string summarizing the protocol</td></tr>
<tr><td><span style="font-weight:bold;">readLength</span></td><td>string</td><td>Read coverage and depth</td></tr>
<tr><td><span style="font-weight:bold;">referenceGenome</span></td><td>object</td><td>Reference genome used for sequencing alignment</td></tr>
<tr><td>referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeAssemblyName</span></td><td>string</td><td>The human readable name of the reference genome</td></tr>
<tr><td>referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeURL</span></td><td>string</td><td>A URL pointing to the location of the reference genome file. (example file types; .fasta, .fa, etc)</td></tr>
<tr><td>referenceGenome<br><span style="font-weight:bold;margin-left:5px">.genomeVersion</span></td><td>string</td><td>the version number of the reference genome</td></tr>
<tr><td><span style="font-weight:bold;">sequencingCenter</span></td><td>string</td><td>Where samples are being sequenced if outsourced</td></tr>
<tr><td><span style="font-weight:bold;">sequencingPlatform</span></td><td>string</td><td>Technology or system used to perform sequencing</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>Units of sequence input (counts, normalized FPKM, RPKM, TPM, TMM)</td></tr>
</table>


 

+ Parameters
    + protocolDbId (Optional, string) ... A unique identifier for a Transcriptomics Protocol
    + observationUnitDbId (Optional, string) ... A unique identifier for an Observation Unit
    + sampleDbId (Optional, string) ... A unique identifier for a field sample
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
                "annotationFile": {
                    "annotationFileName": "Zm-234-Annotations-6.1",
                    "annotationFileURL": "https://phytozome-next.jgi.doe.gov/info/Zmays_Zm_B73_REFERENCE_NAM_5_0_55",
                    "annotationFileVersion": "6.1"
                },
                "countingSoftware": "Salmon",
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
                "instrumentModel": "NextSeq 500",
                "layout": "Paired end",
                "libraryComments": "We used the 3'RNA-seq method",
                "libraryMethod": "3'RNA-seq",
                "mappingSoftware": "HISAT2",
                "nucleicAcidExtractionMethod": "Hot borate",
                "protocolDbId": "f60f15b2",
                "protocolDescription": "Details on sample preparation, calibration, & model used",
                "protocolTitle": "Foss DS3 NIRS protocol for ground butter beans",
                "readLength": "5x depth with 150 bp reads",
                "referenceGenome": {
                    "genomeAssemblyName": "Zm-B73-REFERENCE-NAM-5.0",
                    "genomeURL": "https://www.maizegdb.org/genome/assembly/Zm-B73-REFERENCE-NAM-5.0",
                    "genomeVersion": "5.0"
                },
                "sequencingCenter": "Cornell University Institute of Biotechnology",
                "sequencingPlatform": "Illumina",
                "units": "TPM"
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

