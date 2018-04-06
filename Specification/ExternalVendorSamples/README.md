
# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).


## Plate Details by vendorPlateId [/brapi/v1/vendor/plate/{vendorPlateDbId}] 
Scope: Genotyping facilty.

Response data types
<table>
<thead>
<tr>
<th>Variable</th>
<th>Datatype</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td>metadata</td>
<td>object</td>
<td>pagination, status</td>
<td>Y</td>
</tr>
<tr>
<td>pagination</td>
<td>object</td>
<td>pageSize, currentPage, totalCount, totalPages</td>
<td>Y</td>
</tr>
<tr>
<td>status</td>
<td>list</td>
<td>code, message</td>
<td>Y</td>
</tr>
<tr>
<td>result</td>
<td>Object</td>
<td>Object containing MCPD data</td>
<td>Y</td>
</tr>
<tr>
<td>vendorProjectDbId</td>
<td>string</td>
<td>the name or identifier given to a project by the vendor</td>
<td>Y</td>
</tr>
<tr>
<td>vendorPlateDbId</td>
<td>string</td>
<td>the name or identifier of the plate, given by the vendor</td>
<td>Y</td>
</tr>
<tr>
<td>clientPlateDbId</td>
<td>string</td>
<td>the name of the plate, given by the client</td>
<td>Y</td>
</tr>
<tr>
<td>barcode</td>
<td>string</td>
<td>a string that can be represented as a barcode, identifying this plate</td>
<td>N</td>
</tr>
<tr>
<td>plateFormat</td>
<td>string</td>
<td>defines that plate format, usually Plate_96 or tubes for plateless format</td>
<td>Y</td>
</tr>
<tr>
<td>sampleType</td>
<td>string</td>
<td>DNA or RNA or Tissue, etc.</td>
<td>Y</td>
</tr>
<tr>
<td>status</td>
<td>string</td>
<td>The status of the plate in the processing pipeline. Typically,  &quot;Received&quot;, &quot;Processing&quot;, &quot;QC_passed&quot;, QC_failed&quot;, &quot;Completed&quot; (as per vendor-requirements call)</td>
<td>Y</td>
</tr>
<tr>
<td>samples</td>
<td>Array</td>
<td>list of samples in the plate</td>
<td>Y</td>
</tr>
</tbody>
</table>

 

### Plate Details by vendorPlateId [GET /brapi/v1/vendor/plate/{vendorPlateDbId}] 
+ Parameters
    + vendorPlateDbId (required, string, `8338`) ... The plate ID defined by the vendor

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "vendorProjectDbId": "abc123",
                "vendorPlateDbId": "8338",
                "clientPlateDbId": "def456",
                "vendorBarcode": "",
                "vendorBarcodeImageURL": "",
                "plateFormat": "Plate_96",
                "sampleType": "DNA",
                "status": "(not null)",
                "statusTimeStamp": "2017-06-01 01:57 GMT",
                "samples": [
                    {
                        "sampleDbId": "sample_name",
                        "well": "(optional)",
                        "row": "(optional)",
                        "column": "(optional)",
                        "concentration": "(ng/ul)",
                        "volume": "(ul)",
                        "tissueType": "",
                        "taxonId": {
                            "sourceName": "ncbiTaxon",
                            "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                        }
                    }
                ]
            }
        }

        
## Register plates [/brapi/v1/vendor/plates]

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|Object containing MCPD data|Y|


### Register plates [POST /brapi/v1/vendor/plates] 

Note: if the samples array is empty, plate ID will be returned. Samples can be updated later.

+ Request (application/json)

        {
            "plates": [
                {
                    "vendorProjectDbId": "project_x",
                    "clientPlateDbId": "required",
                    "plateFormat": "Plate_96",
                    "sampleType": "DNA",
                    "samples": [
                        {
                            "sampleDbId": "sample_name",
                            "well": "(optional)",
                            "row": "(optional)",
                            "column": "(optional)",
                            "concentration": "(ng/ul)",
                            "volume": "(ul)",
                            "tissueType": "",
                            "taxonId": {
                                "sourceName": "ncbiTaxon",
                                "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                            }
                        }
                    ]
                }
            ]
        }

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "plates": [
                    {
                        "vendorProjectDbId": "project_x",
                        "vendorPlateDbId": "(not null)",
                        "clientPlateDbId": "(not null)",
                        "vendorBarcode": "(optional)",
                        "vendorBarcodeImageURL": "(optional)",
                        "plateFormat": "Plate_96",
                        "sampleType": "DNA",
                        "status": "",
                        "samples": [
                            {
                                "sampleDbId": "sample_name",
                                "well": "(optional)",
                                "row": "(optional)",
                                "column": "(optional)",
                                "concentration": "(ng/ul)",
                                "volume": "(ul)",
                                "tissueType": "",
                                "taxonId": {
                                    "sourceName": "ncbiTaxon",
                                    "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                                },
                            }
                        ]
                    }
                ]
            }
        }
 
 
 
## Search for plates [/brapi/v1/vendor/plate-search]

Search for plates in the database.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|Object containing MCPD data|Y|
|plates|list|list of plates|
|vendorProjectDbIdg||Y|
|vendorPlateIdentifier|string||Y|
|clientPlateIdentifier|string||Y|
|barcode|string||Y|
|plateFormat|string||Y|
|sampleType|string||Y|
|status|string||Y|
|samples|Object||Y|
|files|Object||Y|
|filename|string||Y|
|url|string||Y|
|md5sum|string||Y|
|filetype|string||Y|
|clientSampleIdentifiers|list||Y|

###  Search for plates [GET /brapi/v1/vendor/plate-search{?vendorProjectDbId}{?vendorPlateDbId}{?clientPlateDbId}{?sampleInfo}{?pageSize}{?page}] 
+ Parameters
     + vendorProjectDbId (optional, string, `8338`) 
     + vendorPlateDbId (optional, string, `8338`)
     + clientPlateDbId (optional, string, `8338`)
     + sampleInfo (optional, boolean, `false`)
     + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
     + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
 
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [
                    {
                        "vendorProjectDbId": "abc123",
                        "vendorPlateDbId": "def456",
                        "clientPlateDbId": "ghi789",
                        "vendorBarcode": "",
                        "vendorBarcodeImageURL": "",
                        "plateFormat": "Plate_96"|"tubes",
                        "sampleType": "DNA"|"RNA"|"Tissue",
                        "status": "(not null)",
                        "statusTimestamp": "2017-06-14 04:02:22 PST",
                        "samples": [],
                        "files": [
                            {
                                "filename": "analysis_results_1",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            },
                            {
                                "filename": "analysis_results_2",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            }
                        ]
                    },
                    {
                        "vendorProjectDbId": "abc123",
                        "vendorPlateDbId": "def456",
                        "clientPlateDbId": "ghi789",
                        "vendorBarcode": "",
                        "vendorBarcodeImageURL": "",
                        "plateFormat": "Plate_96"|"tubes",
                        "sampleType": "DNA"|"RNA"|"Tissue",
                        "status": "(not null)",
                        "statusTimestamp": "2017-06-14 04:02:22 PST",
                        "samples": [],
                        "files": [
                            {
                                "filename": "analysis_results_1",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            },
                            {
                                "filename": "analysis_results_2",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            }
                        ]
                    }
                ]
            }
        }
 
###  Search for plates [POST /brapi/v1/vendor/plate-search] 
+ Request (application/json)

        {
            "vendorProjectDbIds" : ["abc123"],
            "vendorPlateDbIds" : ["def456"],
            "clientPlateDbIds" : ["ghi789"],
            "sampleInfo": "false",
            "page": 0,
            "pageSize": 1000
        }
 
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [
                    {
                        "vendorProjectDbId": "abc123",
                        "vendorPlateDbId": "def456",
                        "clientPlateDbId": "ghi789",
                        "vendorBarcode": "",
                        "vendorBarcodeImageURL": "",
                        "plateFormat": "Plate_96"|"tubes",
                        "sampleType": "DNA"|"RNA"|"Tissue",
                        "status": "(not null)",
                        "statusTimestamp": "2017-06-14 04:02:22 PST",
                        "samples": [],
                        "files": [
                            {
                                "filename": "analysis_results_1",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            },
                            {
                                "filename": "analysis_results_2",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            }
                        ]
                    },
                    {
                        "vendorProjectDbId": "abc123",
                        "vendorPlateDbId": "def456",
                        "clientPlateDbId": "ghi789",
                        "vendorBarcode": "",
                        "vendorBarcodeImageURL": "",
                        "plateFormat": "Plate_96"|"tubes",
                        "sampleType": "DNA"|"RNA"|"Tissue",
                        "status": "(not null)",
                        "statusTimestamp": "2017-06-14 04:02:22 PST",
                        "samples": [],
                        "files": [
                            {
                                "filename": "analysis_results_1",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            },
                            {
                                "filename": "analysis_results_2",
                                "URL": "",
                                "md5sum": "",
                                "fileType": "fastq",
                                "sampleDbIds": [],
                                "additionalInfo": {
                                    
                                }
                            }
                        ]
                    }
                ]
            }
        }
 ## Vendor specification [/brapi/v1/vendor/specifications]

Defines the plate format specification for the vendor.

### Vendor specification [GET /brapi/v1/vendor/specifications]
+ Response 200 (application/json)

        {
            "metadata": {
                "status": [],
                "datafiles": [],
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                }
            },
            "result": {
                "vendorName": "Gene Sequencing Vendor",
                "vendorDescription": "Gene Sequencing Vendor",
                "vendorURL": "www.example.org",
                "contactName": "John Doe",
                "vendorEmail": "jdoe@example.org",
                "vendorPhone": "1-234-567-8910",
                "vendorAddress": "123 Lane St",
                "vendorCity": "Metropolis",
                "vendorCountry": "USA",
                "additionalInfo": {
                    
                },
                "platforms": [
                    {
                        "platformName": "GBS",
                        "platformDescription": "",
                        "platformURL": "",
                        "contactName": "",
                        "contactEmail": "",
                        "contactPhone": "",
                        "shippingAddress": "",
                        "deliverables": [
                            {
                                "name": "",
                                "description": "",
                                "format": ""
                            }
                        ],
                        "standardRequirements": {
                            "minConcentration": "",
                            "maxConcentration": "",
                            "minVolume": "",
                            "maxVolume": "",
                            "minSampleNumber": "",
                            "sampleTypes": [
                                "",
                                ""
                            ],
                            "sampleTypeDetails": "https://...",
                            "inputFormats": [
                                "Plate_96",
                                "Tubes"
                            ],
                            "inputFormatDetails": "https://...",
                            "plateOrientation": "rowFirst|columnFirst",
                            "blankWellPosition": {
                                "positions": [
                                    "random",
                                    "A01",
                                    "H12"
                                ],
                                "numberOfBlanksPerPlate": ""
                            }
                        },
                        "specificRequirements": {
                            
                        },
                        "statuses": [
                            {
                                "statusName": "received",
                                "statusDescription": "Platesarereceivedbyvendor."
                            },
                            {
                                "statusName": "completed",
                                "statusDescription": "Resultfilesareready."
                            },
                            {
                                "statusName": "rejected",
                                "statusDescription": "Platesarerejectedbyvendor"
                            }
                        ],
                        "taxonomyIdSystem": {
                            "name": "NCBITaxonomyId",
                            "URI": "https://..."
                        },
                        "tissueIdSystem": {
                            "name": "DArT",
                            "URI": "https://..."
                        }
                    }
                ]
            }
        }
    
    
 