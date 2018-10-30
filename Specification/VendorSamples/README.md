
# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).




## Vendor [/brapi/v1/vendor] 




### Get Vendor Orders  [GET /brapi/v1/vendor/orders{?orderId}{?submissionId}]

List current available orders

 

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

