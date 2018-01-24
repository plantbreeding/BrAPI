
## Search for plates [ brapi/v1/vendor/plate-search ]

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

###  Search for plates [GET brapi/v1/vendor/plate-search ] 
+ Parameters
     + vendorProjectDbId (optional, string, `8338`) 
     + vendorPlateDbId (optional, string, `8338`)
     + clientPlateDbId (optional, string, `8338`)
     + sampleInfo (optional, boolean, `false`)
     + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
     + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
 
+Response 200 (application/json)

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
