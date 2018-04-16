
### Plate Details by vendorPlateId [GET /brapi/v1/vendor/plates/{vendorPlateDbId}] 
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
