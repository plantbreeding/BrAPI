
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
 
 
 