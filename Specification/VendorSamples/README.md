
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
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the correct billing and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|orderId|string|The order id returned by the vendor when the order was successfully submitted.|
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|serviceId|string|A unique, alpha-numeric ID which identifies the requested service to be used for this order. The service defines what platform, technology, and markers will be used. A list of service IDs can be retrieved from the Vendor Specs.|


 

+ Parameters
    + orderId (Optional, ) ... The order id returned by the vendor when the order was successfully submitted. From response of "POST /vendor/orders"
    + submissionId (Optional, ) ... The submission id returned by the vendor when a set of plates was successfully submitted. From response of "POST /vendor/plates"
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
                "clientId": "clientId0",
                "numberOfSamples": 0,
                "orderId": "orderId0",
                "requiredServiceInfo": {},
                "serviceId": "serviceId0"
            },
            {
                "clientId": "clientId1",
                "numberOfSamples": 0,
                "orderId": "orderId1",
                "requiredServiceInfo": {},
                "serviceId": "serviceId1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Post Vendor Orders  [POST /brapi/v1/vendor/orders]

Submit a new order to a vendor

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|string|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column.|
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|sampleType|string|The type of Samples being submitted|
|serviceIds|array[string]|A list of unique, alpha-numeric ID which identify the requested services to be applied to this order. A Vendor Service defines what platform, technology, and markers will be used. A list of service IDs can be retrieved from the Vendor Specs.|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|orderId|string|A unique, alpha-numeric ID which identifies the order .|
|shipmentForms|array[object]|Array of paper forms which need to be printed and included with the physical shipment|
|fileDescription|string|The human readable long description for this form|
|fileName|string|The human readable name for this form|
|fileURL|string|The URL to download this form|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "clientId0",
    "numberOfSamples": 0,
    "plates": [
        {
            "clientPlateBarcode": "clientPlateBarcode0",
            "clientPlateId": "clientPlateId0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "clientSampleBarCode0",
                    "clientSampleId": "clientSampleId0",
                    "column": "column0",
                    "comments": "comments0",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName0",
                    "row": "row0",
                    "speciesName": "speciesName0",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType0",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well0"
                },
                {
                    "clientSampleBarCode": "clientSampleBarCode1",
                    "clientSampleId": "clientSampleId1",
                    "column": "column1",
                    "comments": "comments1",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName1",
                    "row": "row1",
                    "speciesName": "speciesName1",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType1",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well1"
                }
            ]
        },
        {
            "clientPlateBarcode": "clientPlateBarcode1",
            "clientPlateId": "clientPlateId1",
            "sampleSubmissionFormat": "TUBES",
            "samples": [
                {
                    "clientSampleBarCode": "clientSampleBarCode0",
                    "clientSampleId": "clientSampleId0",
                    "column": "column0",
                    "comments": "comments0",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName0",
                    "row": "row0",
                    "speciesName": "speciesName0",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType0",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well0"
                },
                {
                    "clientSampleBarCode": "clientSampleBarCode1",
                    "clientSampleId": "clientSampleId1",
                    "column": "column1",
                    "comments": "comments1",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName1",
                    "row": "row1",
                    "speciesName": "speciesName1",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType1",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well1"
                }
            ]
        }
    ],
    "requiredServiceInfo": {},
    "sampleType": "DNA",
    "serviceIds": [
        "serviceIds0",
        "serviceIds1"
    ]
}
```



+ Response 200 (application/json)
```
{}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Vendor Orders Plates by orderId  [GET /brapi/v1/vendor/orders/{orderId}/plates]

Retrieve the plate and sample details of an order being processed



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|string|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column.|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
                "clientPlateBarcode": "clientPlateBarcode0",
                "clientPlateId": "clientPlateId0",
                "sampleSubmissionFormat": "PLATE_96",
                "samples": [
                    {
                        "clientSampleBarCode": "clientSampleBarCode0",
                        "clientSampleId": "clientSampleId0",
                        "column": "column0",
                        "comments": "comments0",
                        "concentration": {
                            "units": "units0"
                        },
                        "organismName": "organismName0",
                        "row": "row0",
                        "speciesName": "speciesName0",
                        "taxonomyOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "tissueType": "tissueType0",
                        "tissueTypeOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "volume": {
                            "units": "units0"
                        },
                        "well": "well0"
                    },
                    {
                        "clientSampleBarCode": "clientSampleBarCode1",
                        "clientSampleId": "clientSampleId1",
                        "column": "column1",
                        "comments": "comments1",
                        "concentration": {
                            "units": "units0"
                        },
                        "organismName": "organismName1",
                        "row": "row1",
                        "speciesName": "speciesName1",
                        "taxonomyOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "tissueType": "tissueType1",
                        "tissueTypeOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "volume": {
                            "units": "units0"
                        },
                        "well": "well1"
                    }
                ]
            },
            {
                "clientPlateBarcode": "clientPlateBarcode1",
                "clientPlateId": "clientPlateId1",
                "sampleSubmissionFormat": "TUBES",
                "samples": [
                    {
                        "clientSampleBarCode": "clientSampleBarCode0",
                        "clientSampleId": "clientSampleId0",
                        "column": "column0",
                        "comments": "comments0",
                        "concentration": {
                            "units": "units0"
                        },
                        "organismName": "organismName0",
                        "row": "row0",
                        "speciesName": "speciesName0",
                        "taxonomyOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "tissueType": "tissueType0",
                        "tissueTypeOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "volume": {
                            "units": "units0"
                        },
                        "well": "well0"
                    },
                    {
                        "clientSampleBarCode": "clientSampleBarCode1",
                        "clientSampleId": "clientSampleId1",
                        "column": "column1",
                        "comments": "comments1",
                        "concentration": {
                            "units": "units0"
                        },
                        "organismName": "organismName1",
                        "row": "row1",
                        "speciesName": "speciesName1",
                        "taxonomyOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "tissueType": "tissueType1",
                        "tissueTypeOntologyReference": {
                            "ontologyID": "ontologyID0",
                            "ontologyPrefix": "ontologyPrefix0",
                            "ontologyTerm": "ontologyTerm0"
                        },
                        "volume": {
                            "units": "units0"
                        },
                        "well": "well1"
                    }
                ]
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Vendor Orders Results by orderId  [GET /brapi/v1/vendor/orders/{orderId}/results]

Retrieve the data files generated by the vendors analysis



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|clientSampleIds|array[string]|The list of sampleDbIds included in the file|
|fileName|string|Name of the file|
|fileType|string|Format of the file|
|fileURL|string|The URL to a file with the results of a vendor analysis|
|md5sum|string|MD5 Hash Check Sum for the file to confirm download without error|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
                "additionalInfo": {},
                "clientSampleIds": [
                    "clientSampleIds0",
                    "clientSampleIds1"
                ],
                "fileName": "fileName0",
                "fileType": "fileType0",
                "fileURL": "fileURL0",
                "md5sum": "md5sum0"
            },
            {
                "additionalInfo": {},
                "clientSampleIds": [
                    "clientSampleIds0",
                    "clientSampleIds1"
                ],
                "fileName": "fileName1",
                "fileType": "fileType1",
                "fileURL": "fileURL1",
                "md5sum": "md5sum1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Vendor Orders Status by orderId  [GET /brapi/v1/vendor/orders/{orderId}/status]

Retrieve the current status of an order being processed



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|status|string||


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "status": "registered"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Post Vendor Plates  [POST /brapi/v1/vendor/plates]

Submit a new set of Sample data

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|string|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column.|
|sampleType|string|The type of Samples being submitted|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|submissionId|string|A unique, alpha-numeric ID which identifies a set of plates which have been successfully submitted.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "clientId0",
    "numberOfSamples": 0,
    "plates": [
        {
            "clientPlateBarcode": "clientPlateBarcode0",
            "clientPlateId": "clientPlateId0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "clientSampleBarCode0",
                    "clientSampleId": "clientSampleId0",
                    "column": "column0",
                    "comments": "comments0",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName0",
                    "row": "row0",
                    "speciesName": "speciesName0",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType0",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well0"
                },
                {
                    "clientSampleBarCode": "clientSampleBarCode1",
                    "clientSampleId": "clientSampleId1",
                    "column": "column1",
                    "comments": "comments1",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName1",
                    "row": "row1",
                    "speciesName": "speciesName1",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType1",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well1"
                }
            ]
        },
        {
            "clientPlateBarcode": "clientPlateBarcode1",
            "clientPlateId": "clientPlateId1",
            "sampleSubmissionFormat": "TUBES",
            "samples": [
                {
                    "clientSampleBarCode": "clientSampleBarCode0",
                    "clientSampleId": "clientSampleId0",
                    "column": "column0",
                    "comments": "comments0",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName0",
                    "row": "row0",
                    "speciesName": "speciesName0",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType0",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well0"
                },
                {
                    "clientSampleBarCode": "clientSampleBarCode1",
                    "clientSampleId": "clientSampleId1",
                    "column": "column1",
                    "comments": "comments1",
                    "concentration": {
                        "units": "units0"
                    },
                    "organismName": "organismName1",
                    "row": "row1",
                    "speciesName": "speciesName1",
                    "taxonomyOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "tissueType": "tissueType1",
                    "tissueTypeOntologyReference": {
                        "ontologyID": "ontologyID0",
                        "ontologyPrefix": "ontologyPrefix0",
                        "ontologyTerm": "ontologyTerm0"
                    },
                    "volume": {
                        "units": "units0"
                    },
                    "well": "well1"
                }
            ]
        }
    ],
    "sampleType": "DNA"
}
```



+ Response 200 (application/json)
```
{}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Vendor Plates by submissionId  [GET /brapi/v1/vendor/plates/{submissionId}]

Get data for a submitted set of plates



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|string|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object|Ontology reference details|
|ontologyID|string|Ontology unique ID (example: "0025034" or "4577")|
|ontologyPrefix|string|Ontology identifier prefix (example: "PO" or "NCBITaxon")|
|ontologyTerm|string|Ontology term string (example: "leaf" or "Zea mays")|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column.|


 

+ Parameters
    + submissionId (Required, ) ... 




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
    "result": null
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Vendor Specifications  [GET /brapi/v1/vendor/specifications]

Defines the plate format specification for the vendor.



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary information specific to a particular Vendor. Look for the Vedors specific API documentation for more details|
|services|array[object]|List of platform specifications available at the vendor|
|serviceDescription|string|Description of the vendor platform|
|serviceId|string|Unique identifier for this service|
|serviceName|string|The human readable name of a platform|
|servicePlatformMarkerType|string|The type of markers used in this services platform|
|servicePlatformName|string|The technology platform used by this service|
|specificRequirements|object|Additional arbitrary requirements for a particular platform|
|vendorContact|object||
|vendorAddress|string|The street address of the vendor|
|vendorCity|string|The name of the city where the vendor is located|
|vendorContactName|string|The name or identifier of the primary vendor contact|
|vendorCountry|string|The name of the country where the vendor is located|
|vendorDescription|string|A description of the vendor|
|vendorEmail|string|The primary email address used to contact the vendor|
|vendorName|string|The human readable name of the vendor|
|vendorPhone|string|The primary phone number used to contact the vendor|
|vendorURL|string|The primary URL for the vendor|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "additionalInfo": {},
        "services": [
            {
                "serviceDescription": "serviceDescription0",
                "serviceId": "serviceId0",
                "serviceName": "serviceName0",
                "servicePlatformMarkerType": "FIXED",
                "servicePlatformName": "servicePlatformName0",
                "specificRequirements": {}
            },
            {
                "serviceDescription": "serviceDescription1",
                "serviceId": "serviceId1",
                "serviceName": "serviceName1",
                "servicePlatformMarkerType": "DISCOVERABLE",
                "servicePlatformName": "servicePlatformName1",
                "specificRequirements": {}
            }
        ],
        "vendorContact": {
            "vendorAddress": "vendorAddress0",
            "vendorCity": "vendorCity0",
            "vendorContactName": "vendorContactName0",
            "vendorCountry": "vendorCountry0",
            "vendorDescription": "vendorDescription0",
            "vendorEmail": "vendorEmail0",
            "vendorName": "vendorName0",
            "vendorPhone": "vendorPhone0",
            "vendorURL": "vendorURL0"
        }
    }
}
```

