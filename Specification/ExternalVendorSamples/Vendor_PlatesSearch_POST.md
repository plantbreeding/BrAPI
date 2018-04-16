
### Complex Search for plates [POST /brapi/v1/vendor/plates-search] 
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
