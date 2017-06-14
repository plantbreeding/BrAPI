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
			"plateFormats": ["Plate_96", "Tubes" ],
			"plateOrientation: "rowFirst|columnFirst|NA",		
			"blankWellPosition" : { "definedPositions" :[], numberBlanks:""  }
			"platforms": [
				{
					"platformName" : "GBS", 
					"platformDescription" : "",
					"contactName" : "",
					"contactEmail" : "",
					"contactPhone: "",
					"shippingAddress" : "",
					"Deliverables" :[
						{
							"name": "",
							"description": "",
							"format": "",
							"data" : ""
						},
					], 
					"standardRequirement":
					{
						"minConcentration" : "", 
						"maxConcentration" : "", 
						"minVolume" : "", 
						"maxVolume" : "", 
						"minSampleNumber" : ""
					}
					"specificRequirement":
					{
						"status": [
							{ "statusName": "received", "statusDescription" : "" },
							{ "statusName": "processing", statusDescription: ""},
						],
						"supportedCalls" : [ "token", "vendor-specification" ],	
						"fileFormats" : [{ "name" : "", "description" : ""}],
						"taxonomyIdSystem" : {
							"name": "NCBITaxonomyId" or "DArTTaxonomyId", 
							"URL" : "https://..."
						},
						"tissueIdSystem" : {
							"name": "DArT",
							"URL :  "https://..."
						},
					}
				}
			]
 		}
 	}
 
