## Plate Details by vendorPlateId [ /brapi/v1/vendor/plate/{vendorPlateDbId} ] 
Scope: Genotyping facilty.

##### Response data types

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|Object|Object containing MCPD data|Y|
|vendorProjectDbId|string|the name or identifier given to a project by the vendor|Y|
|vendorPlateDbId|string|the name or identifier of the plate, given by the vendor|Y|
|clientPlateDbId|string|the name of the plate, given by the client|Y|
|barcode|string|a string that can be represented as a barcode, identifying this plate|N|
|plateFormat|string|defines that plate format, usually Plate_96 or tubes for plateless format|Y|
|sampleType|string|DNA or RNA or Tissue, etc.|Y|
|status|string|The status of the plate in the processing pipeline. Typically,  "Received", "Processing", "QC_passed", QC_failed", "Completed" (as per vendor-requirements call)|Y|
|samples|Array|list of samples in the plate|Y|
 

### Plate Details by vendorPlateId [ GET /brapi/v1/vendor/plate/{vendorPlateDbId} ] 
+ Parameters
         + vendorPlateDbId (required, string, `8338`)

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
