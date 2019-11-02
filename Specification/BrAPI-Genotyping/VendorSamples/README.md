
# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).




## Vendor [/brapi/v1/vendor] 




### Get Vendor Orders  [GET /brapi/v1/vendor/orders{?orderId}{?submissionId}]

List current available orders



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the correct billing and contact info.|
|orderId|string|The order id returned by the vendor when the order was successfully submitted.|
|serviceIds|array[string]|A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|


 

+ Parameters
    + orderId (Optional, ) ... The order id returned by the vendor when the order was successfully submitted. From response of "POST /vendor/orders"
    + submissionId (Optional, ) ... The submission id returned by the vendor when a set of plates was successfully submitted. From response of "POST /vendor/plates"
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                    "extractDNA": true,
                    "genus": "Aedes",
                    "species": "vexans",
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





### Post Vendor Orders  [POST /brapi/v1/vendor/orders]

Submit a new order to a vendor

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|samples|array[object]||
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|column|integer|The Column identifier for this samples location in the plate|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|comments|string|Generic comments about this sample for the vendor|
|tissueTypeOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|organismName|string|Scientific organism name|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|row|string|The Row identifier for this samples location in the plate|
|taxonomyOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|speciesName|string|Scientific species name|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|sampleType|string|The type of Samples being submitted|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|serviceIds|array[string]|A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|shipmentForms|array[object]|Array of paper forms which need to be printed and included with the physical shipment|
|fileName|string|The human readable name for this form|
|fileURL|string (uri)|The URL to download this form|
|fileDescription|string|The human readable long description for this form|
|orderId|string|A unique, alpha-numeric ID which identifies the order|


 

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
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
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
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
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
        "genus": "Aedes",
        "species": "vexans",
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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





### Get Vendor Orders Plates by orderId  [GET /brapi/v1/vendor/orders/{orderId}/plates]

Retrieve the plate and sample details of an order being processed



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|samples|array[object]||
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|column|integer|The Column identifier for this samples location in the plate|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|comments|string|Generic comments about this sample for the vendor|
|tissueTypeOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|organismName|string|Scientific organism name|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|row|string|The Row identifier for this samples location in the plate|
|taxonomyOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|speciesName|string|Scientific species name|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                                    "type": [
                                        "OBO",
                                        "RDF",
                                        "WEBPAGE"
                                    ]
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
                                    "type": [
                                        "OBO",
                                        "RDF",
                                        "WEBPAGE"
                                    ]
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





### Get Vendor Orders Results by orderId  [GET /brapi/v1/vendor/orders/{orderId}/results]

Retrieve the data files generated by the vendors analysis



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|fileURL|string (uri)|The URL to a file with the results of a vendor analysis|
|fileType|string|Format of the file|
|md5sum|string|MD5 Hash Check Sum for the file to confirm download without error|
|fileName|string|Name of the file|
|clientSampleIds|array[string]|The list of sampleDbIds included in the file|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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





### Get Vendor Orders Status by orderId  [GET /brapi/v1/vendor/orders/{orderId}/status]

Retrieve the current status of an order being processed



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|status|string||


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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





### Post Vendor Plates  [POST /brapi/v1/vendor/plates]

Submit a new set of Sample data

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|samples|array[object]||
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|column|integer|The Column identifier for this samples location in the plate|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|comments|string|Generic comments about this sample for the vendor|
|tissueTypeOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|organismName|string|Scientific organism name|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|row|string|The Row identifier for this samples location in the plate|
|taxonomyOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|speciesName|string|Scientific species name|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|sampleType|string|The type of Samples being submitted|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|submissionId|string|A unique, alpha-numeric ID which identifies a set of plates which have been successfully submitted.|


 

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
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
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
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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





### Get Vendor Plates by submissionId  [GET /brapi/v1/vendor/plates/{submissionId}]

Get data for a submitted set of plates



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|samples|array[object]||
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|column|integer|The Column identifier for this samples location in the plate|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|comments|string|Generic comments about this sample for the vendor|
|tissueTypeOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|organismName|string|Scientific organism name|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|row|string|The Row identifier for this samples location in the plate|
|taxonomyOntologyReference|object||
|version|string|Ontology version (no specific format)|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|speciesName|string|Scientific species name|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|


 

+ Parameters
    + submissionId (Required, ) ... 




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                                    "type": [
                                        "OBO",
                                        "RDF",
                                        "WEBPAGE"
                                    ]
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
                                    "type": [
                                        "OBO",
                                        "RDF",
                                        "WEBPAGE"
                                    ]
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





### Get Vendor Specifications  [GET /brapi/v1/vendor/specifications]

Defines the plate format specification for the vendor.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary information specific to a particular Vendor. Look for the Vedors specific API documentation for more details|
|services|array[object]|List of platform specifications available at the vendor|
|serviceDescription|string|Description of the vendor platform|
|specificRequirements|array[object]|Additional arbitrary requirements for a particular platform|
|key|string||
|description|string||
|serviceName|string|The human readable name of a platform|
|servicePlatformMarkerType|string|The type of markers used in this services platform|
|servicePlatformName|string|The technology platform used by this service|
|serviceId|string|Unique identifier for this service|
|vendorContact|object||
|vendorURL|string|The primary URL for the vendor|
|vendorDescription|string|A description of the vendor|
|vendorAddress|string|The street address of the vendor|
|vendorEmail|string|The primary email address used to contact the vendor|
|vendorContactName|string|The name or identifier of the primary vendor contact|
|vendorPhone|string|The primary phone number used to contact the vendor|
|vendorCountry|string|The name of the country where the vendor is located|
|vendorCity|string|The name of the city where the vendor is located|
|vendorName|string|The human readable name of the vendor|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                        "description": "The genus of the samples (ex Aedes)",
                        "key": "genus"
                    },
                    {
                        "description": "The species of the samples (ex vexans)",
                        "key": "species"
                    },
                    {
                        "description": "Aproximate volume of each sample (ex 2.3 ml)",
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

