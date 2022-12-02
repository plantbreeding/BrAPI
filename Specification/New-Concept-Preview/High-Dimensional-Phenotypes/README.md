
# Group High-Dimensional Phenotypes

High-Dimensional Phenotypes description




### Get - /metabolomics [GET /brapi/v2/metabolomics{?metabolomicsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Transcriptomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
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
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
</table>


 

+ Parameters
    + metabolomicsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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




### Get - /metabolomics [GET /brapi/v2/metabolomics{?metabolomicsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}/]

Get a filtered list of Transcriptomics Protocols



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
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
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
</table>


 

+ Parameters
    + metabolomicsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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




### Get - /metabolomics/{metabolomicsProtocolDbId} [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}]

Get a single Transcriptomics Protocol by Id. This can be used to quickly get the details of a TranscriptomicsProtocol when you have the Id from another entity.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
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
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
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




### Get - /metabolomics/{metabolomicsProtocolDbId} [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}/]

Get a single Transcriptomics Protocol by Id. This can be used to quickly get the details of a TranscriptomicsProtocol when you have the Id from another entity.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
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
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the Transcriptomics Matrix</td></tr>
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




### Get - /metabolomics/{metabolomicsProtocolDbId}/matrix [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}/matrix{?studyDbId}{?observationUnitDbId}]

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




### Get - /metabolomics/{metabolomicsProtocolDbId}/matrix [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}/matrix{?studyDbId}{?observationUnitDbId}/]

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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">deviceType</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">header_column_names</span></td><td>array[integer]</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the NIRS Matrix</td></tr>
</table>


 

+ Parameters
    + nirsProtocolDbId (Optional, string) ... description
    + observationUnitDbId (Optional, string) ... description
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">deviceType</span></td><td>string</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">header_column_names</span></td><td>array[integer]</td><td>description</td></tr>
<tr><td><span style="font-weight:bold;">protocolDbId</span></td><td>string</td><td>The ID which uniquely identifies the NIRS Matrix</td></tr>
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

