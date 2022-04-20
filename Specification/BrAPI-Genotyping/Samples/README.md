
# Group Samples

API methods for tracking/managing plant samples and related meta-data. A 'Sample' in the context of BrAPI, is defined as the actual biological plant material collected from the field.





### Get - /samples [GET /brapi/v2/samples{?sampleDbId}{?sampleName}{?sampleGroupDbId}{?observationUnitDbId}{?plateDbId}{?plateName}{?germplasmDbId}{?studyDbId}{?trialDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + sampleDbId (Optional, ) ... The unique identifier for a Sample
    + sampleName (Optional, ) ... The human readable name of the sample
    + sampleGroupDbId (Optional, ) ... The unique identifier for a group of related Samples
    + observationUnitDbId (Optional, ) ... The ID which uniquely identifies an observation unit
    + plateDbId (Optional, ) ... The ID which uniquely identifies a plate of samples
    + plateName (Optional, ) ... The human readable name of a plate of samples
    + germplasmDbId (Optional, ) ... The ID which uniquely identifies a germplasm
    + studyDbId (Optional, ) ... The ID which uniquely identifies a study
    + trialDbId (Optional, ) ... The ID which uniquely identifies a trial
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
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
                "additionalInfo": {},
                "column": 6,
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
                "germplasmDbId": "7e08d538",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleDescription": "This sample was taken from the root of a tree",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Post - /samples [POST /brapi/v2/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "column": 6,
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
        "germplasmDbId": "7e08d538",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDescription": "This sample was taken from the root of a tree",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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
                "additionalInfo": {},
                "column": 6,
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
                "germplasmDbId": "7e08d538",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleDescription": "This sample was taken from the root of a tree",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Put - /samples [PUT /brapi/v2/samples/]

Update the details of existing Samples

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<sampleDbId_1>": {
        "additionalInfo": {},
        "column": 6,
        "externalReferences": [],
        "germplasmDbId": "7e08d538",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDescription": "This sample was taken from the root of a tree",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T18:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
    },
    "<sampleDbId_2>": {
        "additionalInfo": {},
        "column": 6,
        "externalReferences": [],
        "germplasmDbId": "7e08d538",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDescription": "This sample was taken from the root of a tree",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T18:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
    }
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
                "additionalInfo": {},
                "column": 6,
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
                "germplasmDbId": "7e08d538",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleDescription": "This sample was taken from the root of a tree",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Get - /samples/{sampleDbId} [GET /brapi/v2/samples/{sampleDbId}]

Used to retrieve the details of a single Sample from a Sample Tracking system.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
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
        "column": 6,
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
        "germplasmDbId": "7e08d538",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleDescription": "This sample was taken from the root of a tree",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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




### **Deprecated** Put - /samples/{sampleDbId} [PUT /brapi/v2/samples/{sampleDbId}/]

**Deprecated in v2.1** Please use `PUT /samples`. Github issue number #462 
<br/>Update the details of an existing Sample

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "column": 6,
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
    "germplasmDbId": "7e08d538",
    "observationUnitDbId": "073a3ce5",
    "plateDbId": "2dce16d1",
    "plateName": "Plate_alpha_20191022",
    "programDbId": "bd748e00",
    "row": "B",
    "sampleBarcode": "3a027b59",
    "sampleDescription": "This sample was taken from the root of a tree",
    "sampleGroupDbId": "8524b436",
    "sampleName": "Sample_alpha_20191022",
    "samplePUI": "doi:10.15454/312953986E3",
    "sampleTimestamp": "2018-01-01T14:47:23-0600",
    "sampleType": "Tissue",
    "studyDbId": "64bd6bf9",
    "takenBy": "Bob",
    "tissueType": "Root",
    "trialDbId": "d34c5349",
    "well": "B6"
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
        "additionalInfo": {},
        "column": 6,
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
        "germplasmDbId": "7e08d538",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleDescription": "This sample was taken from the root of a tree",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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




### Post - /search/samples [POST /brapi/v2/search/samples]

Submit a search request for `Samples`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/samples/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>commonCropNames</td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td>externalReferenceIDs</td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceIds</td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceSources</td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td>germplasmDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>germplasmNames</td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td>observationUnitDbIds</td><td>array[string]</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>page</td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td>pageSize</td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td>plateDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateNames</td><td>array[string]</td><td>The human readable name of a plate of samples</td></tr>
<tr><td>programDbIds</td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>programNames</td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>sampleDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a sample</td></tr>
<tr><td>sampleGroupDbIds</td><td>array[string]</td><td>The unique identifier for a group of related Samples</td></tr>
<tr><td>sampleNames</td><td>array[string]</td><td>The human readable name of the sample</td></tr>
<tr><td>studyDbIds</td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td>studyNames</td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td>trialDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td>trialNames</td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
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
    "germplasmDbIds": [
        "d745e1e2",
        "6dd28d74"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
    ],
    "observationUnitDbIds": [
        "3cd0ca36",
        "983f3b14"
    ],
    "page": 0,
    "pageSize": 1000,
    "plateDbIds": [
        "0cac98b8",
        "b96125fb"
    ],
    "plateNames": [
        "0cac98b8",
        "b96125fb"
    ],
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "sampleDbIds": [
        "3bece2ca",
        "dd286cc6"
    ],
    "sampleGroupDbIds": [
        "45e1e2d7",
        "6cc6dd28"
    ],
    "sampleNames": [
        "SA_111",
        "SA_222"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
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
                "additionalInfo": {},
                "column": 6,
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
                "germplasmDbId": "7e08d538",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleDescription": "This sample was taken from the root of a tree",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Get - /search/samples/{searchResultsDbId} [GET /brapi/v2/search/samples/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Samples` search request <br/>
Clients should submit a search request using the corresponding `POST /search/samples` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>column</td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>germplasmDbId</td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observationUnitDbId</td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>plateDbId</td><td>string</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td>plateName</td><td>string</td><td>The human readable name of a plate</td></tr>
<tr><td>programDbId</td><td>string</td><td>The ID which uniquely identifies a program within the given database server</td></tr>
<tr><td>row</td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>sampleBarcode</td><td>string</td><td>A unique identifier physically attached to the sample</td></tr>
<tr><td>sampleDbId</td><td>string</td><td>The ID which uniquely identifies a sample  MIAPPE V1.1 (DM-76) Sample ID - Unique identifier for the sample.</td></tr>
<tr><td>sampleDescription</td><td>string</td><td>Description of a sample  MIAPPE V1.1 (DM-79) Sample description - Any information not captured by the other sample fields, including quantification, sample treatments and processing.</td></tr>
<tr><td>sampleGroupDbId</td><td>string</td><td>The ID which uniquely identifies a group of samples</td></tr>
<tr><td>sampleName</td><td>string</td><td>The human readable name of the sample</td></tr>
<tr><td>samplePUI</td><td>string</td><td>A permanent unique identifier for the sample (DOI, URL, UUID, etc)  MIAPPE V1.1 (DM-81) External ID - An identifier for the sample in a persistent repository, comprising the name of the repository and the accession number of the observation unit therein. Submission to the EBI Biosamples repository is recommended. URI are recommended when possible. </td></tr>
<tr><td>sampleTimestamp</td><td>string (date-time)</td><td>The date and time a sample was collected from the field  MIAPPE V1.1 (DM-80) Collection date - The date and time when the sample was collected / harvested</td></tr>
<tr><td>sampleType</td><td>string</td><td>The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>takenBy</td><td>string</td><td>The name or identifier of the entity which took the sample from the field</td></tr>
<tr><td>tissueType</td><td>string</td><td>The type of tissue sampled. ex. 'Leaf', 'Root', etc.  MIAPPE V1.1 (DM-78) Plant anatomical entity - A description of  the plant part (e.g. leaf) or the plant product (e.g. resin) from which the sample was taken, in the form of an accession number to a suitable controlled vocabulary (Plant Ontology).</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial within the given database server</td></tr>
<tr><td>well</td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

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
                "additionalInfo": {},
                "column": 6,
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
                "germplasmDbId": "7e08d538",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleDescription": "This sample was taken from the root of a tree",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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

