
# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).





### Get - /vendor/orders [GET /brapi/v2/vendor/orders{?orderId}{?submissionId}{?page}{?pageSize}]

List current available orders



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">clientId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the correct billing and contact info.</td></tr>
<tr><td><span style="font-weight:bold;">numberOfSamples</span></td><td>integer</td><td>The total number of samples contained in this request. Used for billing and basic validation of the request.</td></tr>
<tr><td><span style="font-weight:bold;">orderId</span></td><td>string</td><td>The order id returned by the vendor when the order was successfully submitted.</td></tr>
<tr><td><span style="font-weight:bold;">requiredServiceInfo</span></td><td>object</td><td>A map of additional data required by the requested service. This includes things like Volume and Concentration.</td></tr>
<tr><td><span style="font-weight:bold;">serviceIds</span></td><td>array[string]</td><td>A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.</td></tr>
</table>


 

+ Parameters
    + orderId (Optional, ) ... The order id returned by the vendor when the order was successfully submitted. From response of "POST /vendor/orders"
    + submissionId (Optional, ) ... The submission id returned by the vendor when a set of plates was successfully submitted. From response of "POST /vendor/plates"
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
                "clientId": "7b51ad15",
                "numberOfSamples": 180,
                "orderId": "96ba0ca3",
                "requiredServiceInfo": {
                    "extractDNA": "true",
                    "genus": "Zea",
                    "species": "mays",
                    "volumePerWell": "2.3 ml"
                },
                "serviceIds": [
                    "e8f60f64",
                    "05bd925a",
                    "b698fb5e"
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




### Post - /vendor/orders [POST /brapi/v2/vendor/orders]

Submit a new order to a vendor

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">clientId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.</td></tr>
<tr><td><span style="font-weight:bold;">numberOfSamples</span></td><td>integer</td><td>The total number of samples contained in this request. Used for billing and basic validation of the request.</td></tr>
<tr><td><span style="font-weight:bold;">plates</span></td><td>array[object]</td><td>Array of new plates to be submitted to a vendor</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateBarcode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this plate</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateId</span></td><td>string</td><td>The ID which uniquely identifies this plate to the client making the request</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.sampleSubmissionFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.samples</span></td><td>array[object]</td><td></td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleBarCode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this sample</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleId</span></td><td>string</td><td>The ID which uniquely identifies this sample to the client making the request</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.column</span></td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Generic comments about this sample for the vendor</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.concentration</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.organismName</span></td><td>string</td><td>Scientific organism name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.speciesName</span></td><td>string</td><td>Scientific species name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.taxonomyOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueTypeOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.volume</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.well</span></td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
<tr><td><span style="font-weight:bold;">requiredServiceInfo</span></td><td>object</td><td>A map of additional data required by the requested service. This includes things like Volume and Concentration.</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of Samples being submitted</td></tr>
<tr><td><span style="font-weight:bold;">serviceIds</span></td><td>array[string]</td><td>A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">orderId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies the order</td></tr>
<tr><td><span style="font-weight:bold;">shipmentForms</span></td><td>array[object]</td><td>Array of paper forms which need to be printed and included with the physical shipment</td></tr>
<tr><td>shipmentForms<br><span style="font-weight:bold;margin-left:5px">.fileDescription</span></td><td>string</td><td>The human readable long description for this form</td></tr>
<tr><td>shipmentForms<br><span style="font-weight:bold;margin-left:5px">.fileName</span></td><td>string</td><td>The human readable name for this form</td></tr>
<tr><td>shipmentForms<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>The URL to download this form</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "b8aac350",
    "numberOfSamples": 180,
    "plates": [
        {
            "clientPlateBarcode": "6ebf3f25",
            "clientPlateId": "02a8d6f0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "7c07e527",
                    "clientSampleId": "bd96bd69",
                    "column": 6,
                    "comments": "This is my favorite sample, please be extra careful with it.",
                    "concentration": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "organismName": "Aspergillus fructus",
                    "row": "B",
                    "speciesName": "Aspergillus fructus",
                    "taxonomyOntologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": "OBO"
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "tissueType": "Root",
                    "tissueTypeOntologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": "OBO"
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "volume": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "well": "B6"
                }
            ]
        }
    ],
    "requiredServiceInfo": {
        "extractDNA": true,
        "genus": "Zea",
        "species": "mays",
        "volumePerWell": "2.3 ml"
    },
    "sampleType": "Tissue",
    "serviceIds": [
        "e8f60f64",
        "05bd925a",
        "b698fb5e"
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
        "orderId": "b5144468",
        "shipmentForms": [
            {
                "fileDescription": "This is a shipment manifest form",
                "fileName": "Shipment Manifest",
                "fileURL": "https://vendor.org/forms/manifest.pdf"
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




### Get - /vendor/orders/{orderId}/plates [GET /brapi/v2/vendor/orders/{orderId}/plates{?page}{?pageSize}]

Retrieve the plate and sample details of an order being processed



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">clientPlateBarcode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this plate</td></tr>
<tr><td><span style="font-weight:bold;">clientPlateId</span></td><td>string</td><td>The ID which uniquely identifies this plate to the client making the request</td></tr>
<tr><td><span style="font-weight:bold;">sampleSubmissionFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">samples</span></td><td>array[object]</td><td></td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleBarCode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this sample</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleId</span></td><td>string</td><td>The ID which uniquely identifies this sample to the client making the request</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.column</span></td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Generic comments about this sample for the vendor</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.concentration</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.organismName</span></td><td>string</td><td>Scientific organism name</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.speciesName</span></td><td>string</td><td>Scientific species name</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.taxonomyOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.tissueTypeOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.volume</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>samples<br><span style="font-weight:bold;margin-left:5px">.well</span></td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
                "clientPlateBarcode": "31dd5787",
                "clientPlateId": "0ad6c0ef",
                "sampleSubmissionFormat": "PLATE_96",
                "samples": [
                    {
                        "clientSampleBarCode": "7c07e527",
                        "clientSampleId": "bd96bd69",
                        "column": 6,
                        "comments": "This is my favorite sample, please be extra careful with it.",
                        "concentration": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "organismName": "Aspergillus fructus",
                        "row": "B",
                        "speciesName": "Aspergillus fructus",
                        "taxonomyOntologyReference": {
                            "documentationLinks": [
                                {
                                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                    "type": "OBO"
                                }
                            ],
                            "ontologyDbId": "6b071868",
                            "ontologyName": "The Crop Ontology",
                            "version": "7.2.3"
                        },
                        "tissueType": "Root",
                        "tissueTypeOntologyReference": {
                            "documentationLinks": [
                                {
                                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                    "type": "OBO"
                                }
                            ],
                            "ontologyDbId": "6b071868",
                            "ontologyName": "The Crop Ontology",
                            "version": "7.2.3"
                        },
                        "volume": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "well": "B6"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /vendor/orders/{orderId}/results [GET /brapi/v2/vendor/orders/{orderId}/results{?page}{?pageSize}]

Retrieve the data files generated by the vendors analysis



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">clientSampleIds</span></td><td>array[string]</td><td>The list of sampleDbIds included in the file</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>Name of the file</td></tr>
<tr><td><span style="font-weight:bold;">fileType</span></td><td>string</td><td>Format of the file</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string<br>(uri)</td><td>The URL to a file with the results of a vendor analysis</td></tr>
<tr><td><span style="font-weight:bold;">md5sum</span></td><td>string</td><td>MD5 Hash Check Sum for the file to confirm download without error</td></tr>
</table>


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
                "clientSampleIds": [
                    "3968733e",
                    "e0de6391",
                    "66854172"
                ],
                "fileName": "sequence_data_ce640bd3.csv",
                "fileType": "text/csv",
                "fileURL": "https://vendor.org/data/sequence_data_ce640bd3.csv",
                "md5sum": "c2365e900c81a89cf74d83dab60df146"
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




### Get - /vendor/orders/{orderId}/status [GET /brapi/v2/vendor/orders/{orderId}/status]

Retrieve the current status of an order being processed



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td></td></tr>
</table>


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
        "status": [
            "registered",
            "received",
            "inProgress",
            "completed",
            "rejected"
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




### Post - /vendor/plates [POST /brapi/v2/vendor/plates]

Submit a new set of Sample data

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">clientId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.</td></tr>
<tr><td><span style="font-weight:bold;">numberOfSamples</span></td><td>integer</td><td>The total number of samples contained in this request. Used for billing and basic validation of the request.</td></tr>
<tr><td><span style="font-weight:bold;">plates</span></td><td>array[object]</td><td>Array of new plates to be submitted to a vendor</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateBarcode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this plate</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateId</span></td><td>string</td><td>The ID which uniquely identifies this plate to the client making the request</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.sampleSubmissionFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.samples</span></td><td>array[object]</td><td></td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleBarCode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this sample</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleId</span></td><td>string</td><td>The ID which uniquely identifies this sample to the client making the request</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.column</span></td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Generic comments about this sample for the vendor</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.concentration</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.organismName</span></td><td>string</td><td>Scientific organism name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.speciesName</span></td><td>string</td><td>Scientific species name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.taxonomyOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueTypeOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.volume</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.well</span></td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of Samples being submitted</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">submissionId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies a set of plates which have been successfully submitted.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "b8aac350",
    "numberOfSamples": 180,
    "plates": [
        {
            "clientPlateBarcode": "6ebf3f25",
            "clientPlateId": "02a8d6f0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "7c07e527",
                    "clientSampleId": "bd96bd69",
                    "column": 6,
                    "comments": "This is my favorite sample, please be extra careful with it.",
                    "concentration": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "organismName": "Aspergillus fructus",
                    "row": "B",
                    "speciesName": "Aspergillus fructus",
                    "taxonomyOntologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": "OBO"
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "tissueType": "Root",
                    "tissueTypeOntologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": "OBO"
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "volume": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "well": "B6"
                }
            ]
        }
    ],
    "sampleType": "Tissue"
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
        "submissionId": "f8f409e0"
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




### Get - /vendor/plates/{submissionId} [GET /brapi/v2/vendor/plates/{submissionId}]

Get data for a submitted set of plates



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">clientId</span></td><td>string</td><td>A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.</td></tr>
<tr><td><span style="font-weight:bold;">numberOfSamples</span></td><td>integer</td><td>The total number of samples contained in this request. Used for billing and basic validation of the request.</td></tr>
<tr><td><span style="font-weight:bold;">plates</span></td><td>array[object]</td><td>Array of new plates to be submitted to a vendor</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateBarcode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this plate</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.clientPlateId</span></td><td>string</td><td>The ID which uniquely identifies this plate to the client making the request</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.sampleSubmissionFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td>plates<br><span style="font-weight:bold;margin-left:5px">.samples</span></td><td>array[object]</td><td></td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleBarCode</span></td><td>string</td><td>(Optional) The value of the bar code attached to this sample</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.clientSampleId</span></td><td>string</td><td>The ID which uniquely identifies this sample to the client making the request</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.column</span></td><td>integer</td><td>The Column identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.comments</span></td><td>string</td><td>Generic comments about this sample for the vendor</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.concentration</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.concentration<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.organismName</span></td><td>string</td><td>Scientific organism name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.row</span></td><td>string</td><td>The Row identifier for this samples location in the plate</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.speciesName</span></td><td>string</td><td>Scientific species name</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.taxonomyOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.taxonomyOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueType</span></td><td>string</td><td>The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.tissueTypeOntologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>plates<br>.samples<br>.tissueTypeOntologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.volume</span></td><td>object</td><td>A value with units</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>Units (example: "ng/ul")</td></tr>
<tr><td>plates<br>.samples<br>.volume<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>number</td><td>Value (example: "2.3")</td></tr>
<tr><td>plates<br>.samples<br><span style="font-weight:bold;margin-left:5px">.well</span></td><td>string</td><td>The Well identifier for this samples location in the plate. Usually a concatenation of Row and Column, or just a number if the samples are not part of an ordered plate.</td></tr>
</table>


 

+ Parameters
    + submissionId (Required, ) ... The submission id returned by the vendor when a set of plates was successfully submitted. From response of "POST /vendor/plates"
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
        "clientId": "e470ae0d",
        "numberOfSamples": 180,
        "plates": [
            {
                "clientPlateBarcode": "bfb33593",
                "clientPlateId": "dae8f49d",
                "sampleSubmissionFormat": "PLATE_96",
                "samples": [
                    {
                        "clientSampleBarCode": "7c07e527",
                        "clientSampleId": "bd96bd69",
                        "column": 6,
                        "comments": "This is my favorite sample, please be extra careful with it.",
                        "concentration": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "organismName": "Aspergillus fructus",
                        "row": "B",
                        "speciesName": "Aspergillus fructus",
                        "taxonomyOntologyReference": {
                            "documentationLinks": [
                                {
                                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                    "type": "OBO"
                                }
                            ],
                            "ontologyDbId": "6b071868",
                            "ontologyName": "The Crop Ontology",
                            "version": "7.2.3"
                        },
                        "tissueType": "Root",
                        "tissueTypeOntologyReference": {
                            "documentationLinks": [
                                {
                                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                    "type": "OBO"
                                }
                            ],
                            "ontologyDbId": "6b071868",
                            "ontologyName": "The Crop Ontology",
                            "version": "7.2.3"
                        },
                        "volume": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "well": "B6"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /vendor/specifications [GET /brapi/v2/vendor/specifications]

Defines the plate format specification for the vendor.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">services</span></td><td>array[object]</td><td>List of platform specifications available at the vendor</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.serviceDescription</span></td><td>string</td><td>Description of the vendor platform</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.serviceId</span></td><td>string</td><td>Unique identifier for this service</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.serviceName</span></td><td>string</td><td>The human readable name of a platform</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.servicePlatformMarkerType</span></td><td>string</td><td>The type of markers used in this services platform</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.servicePlatformName</span></td><td>string</td><td>The technology platform used by this service</td></tr>
<tr><td>services<br><span style="font-weight:bold;margin-left:5px">.specificRequirements</span></td><td>array[object]</td><td>Additional arbitrary requirements for a particular platform</td></tr>
<tr><td>services<br>.specificRequirements<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>The value of a key-value entry in a map of Vendor specific requirements</td></tr>
<tr><td>services<br>.specificRequirements<br><span style="font-weight:bold;margin-left:5px">.key</span></td><td>string</td><td>The key of a key-value entry in a map of Vendor specific requirements</td></tr>
<tr><td><span style="font-weight:bold;">vendorContact</span></td><td>object</td><td></td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorAddress</span></td><td>string</td><td>The street address of the vendor</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorCity</span></td><td>string</td><td>The name of the city where the vendor is located</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorContactName</span></td><td>string</td><td>The name or identifier of the primary vendor contact</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorCountry</span></td><td>string</td><td>The name of the country where the vendor is located</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorDescription</span></td><td>string</td><td>A description of the vendor</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorEmail</span></td><td>string</td><td>The primary email address used to contact the vendor</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorName</span></td><td>string</td><td>The human readable name of the vendor</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorPhone</span></td><td>string</td><td>The primary phone number used to contact the vendor</td></tr>
<tr><td>vendorContact<br><span style="font-weight:bold;margin-left:5px">.vendorURL</span></td><td>string</td><td>The primary URL for the vendor</td></tr>
</table>


 

+ Parameters
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
        "services": [
            {
                "serviceDescription": "A combined DNA extract and Sequencing process using technology and science. Lots of automated pipet machines.",
                "serviceId": "085d298f",
                "serviceName": "The Deluxe Service",
                "servicePlatformMarkerType": "FIXED",
                "servicePlatformName": "RNA-seq",
                "specificRequirements": [
                    {
                        "description": "The genus of the samples",
                        "key": "genus"
                    },
                    {
                        "description": "The species of the samples",
                        "key": "species"
                    },
                    {
                        "description": "Approximate volume of each sample (ex 2.3 ml)",
                        "key": "volumePerWell"
                    },
                    {
                        "description": "Does DNA extraction need to happen before sequencing (ex true)",
                        "key": "extractDNA"
                    }
                ]
            }
        ],
        "vendorContact": {
            "vendorAddress": "123 Main Street",
            "vendorCity": "Townsville",
            "vendorContactName": "Bob Robertson",
            "vendorCountry": "USA",
            "vendorDescription": "This is a sequencing vendor. Sequencing happens here.",
            "vendorEmail": "bob@bob.org",
            "vendorName": "The Example Vendor Lab",
            "vendorPhone": "+1-800-555-5555",
            "vendorURL": "https://sequencing.org/vendor"
        }
    }
}
```

