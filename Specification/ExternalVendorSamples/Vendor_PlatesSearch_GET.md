
### Simple Search for plates [GET /brapi/v1/vendor/plates-search{?vendorProjectDbId}{?vendorPlateDbId}{?clientPlateDbId}{?sampleInfo}{?pageSize}{?page}] 
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
