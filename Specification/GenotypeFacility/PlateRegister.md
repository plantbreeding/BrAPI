
## Register plate(s) [ /brapi/v2/plate-register ]

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|Object containing MCPD data|Y|


### Register plates [ /brapi/v2/plate-register ] POST


Note: if the samples array is empty, plate ID will be returned. Samples can be updated later.
+Request (must be an array of plates, can submit multiple plates)

        {
                "token" : '',
                "plates":[ { 
                        "vendorProjectIdentifier" : "project_x", 
                               "clientPlateIdentifier" : "required",
                        "plateFormat" : "Plate_96" | "tubes",  // see vendor restrictions call!
                        "sampleType" : "DNA" | "RNA" | "Tissue", 
                        "samples" :[
                                {
                                        "clientSampleIdentifier" : "sample_name", 
                                        "well" :  "(optional)",
                                        "row" : "(optional)",
                                        "column": "(optional)",                        
                                        "concentration": "(ng/ul)",
                                        "volume": "(ul)",
                                        "taxomonyId" : 4554,
                                        "tissueType" : "" 
                                }
                        ] 
                }
                ]
        }
 
+Response

        {
                "metadata": {   
                        "status": [ {"code": "",  "message" : "info message"}],
                        "datafiles": []
                    },
                    "result" : { 
                            "responseURL " : "",
                            "plates" : [
                                    {
                                            "vendorProjectIdentifier" : "project_x", 
                                            "vendorPlateIdentifier" : "(not null)",
                                            "clientPlateIdentifier" : "(not null)",
                                            "vendorBarcode" : "(optional)",
                                            "vendorBarcodeImageURL" : "(optional)",
                                            "plateFormat" : "Plate_96" | "tubes",
                                            "sampleType" : "DNA" | "RNA" | "Tissue",
                                            "status" : "",
                                            "samples" :[
                                                    {
                                                            "clientSampleIdentifier": "sample_name1", 
                                                            "well" : "(optional)",
                                                            "row" : "(optional)",
                                                            "column" : "(optional)",
                                                            "concentration" : "(ng/ul)",
                                                            "volume" : "(ul)",
                                                            "taxomonyId" : "",
                                                            "tissueType" : "" 
                                                    }
                                            ]
                                   }        
                            ]
                   }
        }
 
 
