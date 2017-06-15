## Vendor specification [ /brapi/v2/vendor-specification ]

Defines the plate format specification for the vendor.

### Vendor specification [ /brapi/v2/vendor-requirement ] GET

+Request

+Response
        {
                "metadata" : {   
                        "status": [],
                        "datafiles": []
                },
                "result" : {
                        "vendorName" : "",
                        "vendorDescription" : "",
                        "vendorURL" : "",
                        "contactName" : "",
                        "vendorEmail" : "",
                        "vendorPhone" : "",
                        "vendorAddress" : "",
                        "vendorCity" : "",
                        "vendorCountry" : "",
                        "additionalInfo" : {}, 
                
                        "platforms": [
                                {
                                        "platformName" : "GBS", 
                                        "platformDescription" : "",
                                        "platformURL" : "",
                                        "contactName" : "",
                                        "contactEmail" : "",
                                        "contactPhone: "",
                                        "shippingAddress" : "",
                                        "deliverables" :[
                                                {
                                                        "name": "",
                                                        "description": "",
                                                        "format": "",
                                                },
                                        ], 
                                        "standardRequirements":
                                        {
                                                "minConcentration" : "", 
                                                "maxConcentration" : "", 
                                                "minVolume" : "", 
                                                "maxVolume" : "", 
                                                "minSampleNumber" : ""
                                                "sampleTypes" :[ "", ""  ],
                                                "sampleTypeDetails" : "https://...",
                                                "inputFormats" : [ "Plate_96", "Tubes", "..." ],
                                                "inputFormatDetails" : "https://...",
                                                "plateOrientation" : "rowFirst|columnFirst",
                                                "blankWellPosition" :{
                                                        "positions" : [ "random" or "A01", "H12"], 
                                                        "numberOfBlanksPerPlate" : "",
                                                }
                                         },
                                        "specificRequirement": {

                                        },
                                        "statuses" : [
        //Required statuses
                                                { 
                                                        { "statusName" : "received", "statusDescription" : "Plates are received by vendor." },
                                                        { "statusName": "completed", "statusDescription" : "Result files are ready." },
                                                        { "statusName": "rejected", "statusDescription" : "Plates are rejected by vendor" },
        //Extra statuses are optional
                                                }
                                        ],
 
                                        "taxonomyIdSystem" : {
                                                "name" : "NCBITaxonomyId" or "DArTTaxonomyId", 
                                                "URI" : "https://..."
                                        },
 
                                        "tissueIdSystem" : {
                                                "name" : "DArT",
                                                "URI": "https://..."
                                        },

                                }
                        ]
                 }
         }
 
