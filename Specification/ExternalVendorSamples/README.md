
# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).




## Vendor/plates-search [Get /brapi/v1/vendor/plates-search{?vendorProjectDbId}{?vendorPlateDbId}{?clientPlateDbId}{?sampleInfo}{?pageSize}{?page}]

Search for plates in the database.

<a href="https://test-server.brapi.org/brapi/v1/vendor/plates-search"> test-server.brapi.org/brapi/v1/vendor/plates-search</a> 

+ Parameters
    + vendorProjectDbId (Optional, string) ... 
    + vendorPlateDbId (Optional, string) ... 
    + clientPlateDbId (Optional, string) ... 
    + sampleInfo (Optional, boolean) ... 
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.




## Vendor/plates-search [Post /brapi/v1/vendor/plates-search]

Search for plates in the database.

<a href="https://test-server.brapi.org/brapi/v1/vendor"> test-server.brapi.org/brapi/v1/vendor/plate-search</a> 

+ Parameters
 
+ Request (application/json)
/definitions/vendorPlateSearchRequest



## Vendor/plates/{vendorplatedbid} [Get /brapi/v1/vendor/plates/{vendorPlateDbId}]

 Response data types 
 <table> <thead> <tr> <th>Variable</th> <th>Datatype</th> <th>Description</th> <th>Required</th> </tr> </thead> <tbody> <tr> <td>metadata</td> <td>object</td> <td>pagination, status</td> <td>Y</td> </tr> <tr> <td>pagination</td> <td>object</td> <td>pageSize, currentPage, totalCount, totalPages</td> <td>Y</td> </tr> <tr> <td>status</td> <td>list</td> <td>code, message</td> <td>Y</td> </tr> <tr> <td>result</td> <td>Object</td> <td>Object containing MCPD data</td> <td>Y</td> </tr> <tr> <td>vendorProjectDbId</td> <td>string</td> <td>the name or identifier given to a project by the vendor</td> <td>Y</td> </tr> <tr> <td>vendorPlateDbId</td> <td>string</td> <td>the name or identifier of the plate, given by the vendor</td> <td>Y</td> </tr> <tr> <td>clientPlateDbId</td> <td>string</td> <td>the name of the plate, given by the client</td> <td>Y</td> </tr> <tr> <td>barcode</td> <td>string</td> <td>a string that can be represented as a barcode, identifying this plate</td> <td>N</td> </tr> <tr> <td>plateFormat</td> <td>string</td> <td>defines that plate format, usually Plate_96 or tubes for plateless format</td> <td>Y</td> </tr> <tr> <td>sampleType</td> <td>string</td> <td>DNA or RNA or Tissue, etc.</td> <td>Y</td> </tr> <tr> <td>status</td> <td>string</td> <td>The status of the plate in the processing pipeline. Typically,  &quot;Received&quot;, &quot;Processing&quot;, &quot;QC_passed&quot;, QC_failed&quot;, &quot;Completed&quot; (as per vendor-requirements call)</td> <td>Y</td> </tr> <tr> <td>samples</td> <td>Array</td> <td>list of samples in the plate</td> <td>Y</td> </tr> </tbody> </table>
 <a href="https://test-server.brapi.org/brapi/v1/vendor"> test-server.brapi.org/brapi/v1/vendor/plate/{vendorPlateDbId}</a> 

+ Parameters
    + vendorPlateDbId (Required, string) ... The plate ID defined by the vendor


+ Response 200 (application/json)
```
{
    "result": {
        "samples": [
            {
                "well": "(optional)",
                "sampleDbId": "sample_name",
                "column": "(optional)",
                "taxonId": {
                    "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                    "sourceName": "ncbiTaxon"
                },
                "tissueType": "",
                "row": "(optional)",
                "volume": "(ul)",
                "concentration": "(ng/ul)"
            }
        ],
        "vendorPlateDbId": "8338",
        "vendorProjectDbId": "abc123",
        "statusTimeStamp": "2017-06-01 01:57 GMT",
        "plateFormat": "Plate_96",
        "sampleType": "DNA",
        "vendorBarcodeImageURL": "",
        "status": "(not null)",
        "vendorBarcode": "",
        "clientPlateDbId": "def456"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```

## Vendor/plates [Post /brapi/v1/vendor/plates]

Note: if the samples array is empty, plate ID will be returned.
Samples can be updated later. 

+ Parameters
 
+ Request (application/json)
/definitions/vendorPlateRequest



## Vendor/specifications [Get /brapi/v1/vendor/specifications]

 Defines the plate format specification for the vendor.
<a href="https://test-server.brapi.org/brapi/v1/vendor"> test-server.brapi.org/brapi/v1/vendor/specifications</a> 

+ Parameters


+ Response 200 (application/json)
```
{
    "result": {
        "vendorPhone": "1-234-567-8910",
        "vendorCity": "Metropolis",
        "vendorEmail": "jdoe@example.org",
        "vendorAddress": "123 Lane St",
        "vendorName": "Gene Sequencing Vendor",
        "vendorURL": "www.example.org",
        "vendorCountry": "USA",
        "vendorDescription": "Gene Sequencing Vendor",
        "platforms": [
            {
                "contactEmail": "",
                "specificRequirements": {},
                "deliverables": [
                    {
                        "format": "",
                        "name": "",
                        "description": ""
                    }
                ],
                "platformDescription": "",
                "contactPhone": "",
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
                "contactName": "",
                "tissueIdSystem": {
                    "name": "DArT",
                    "URI": "https://..."
                },
                "shippingAddress": "",
                "taxonomyIdSystem": {
                    "name": "NCBITaxonomyId",
                    "URI": "https://..."
                },
                "platformURL": "",
                "standardRequirements": {
                    "minVolume": "",
                    "minSampleNumber": "",
                    "maxVolume": "",
                    "plateOrientation": "rowFirst|columnFirst",
                    "inputFormatDetails": "https://...",
                    "minConcentration": "",
                    "sampleTypes": [
                        "",
                        ""
                    ],
                    "sampleTypeDetails": "https://...",
                    "maxConcentration": "",
                    "blankWellPosition": {
                        "positions": [
                            "random",
                            "A01",
                            "H12"
                        ],
                        "numberOfBlanksPerPlate": ""
                    },
                    "inputFormats": [
                        "Plate_96",
                        "Tubes"
                    ]
                },
                "platformName": "GBS"
            }
        ],
        "contactName": "John Doe",
        "additionalInfo": {}
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```