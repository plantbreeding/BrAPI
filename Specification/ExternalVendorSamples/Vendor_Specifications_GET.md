## Vendor specification [ /brapi/v1/vendor/specifications ]

Defines the plate format specification for the vendor.

### Vendor specification [ GET /brapi/v1/vendor/specifications ]
+Request

+Response 200 (application/json)

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
    
    
