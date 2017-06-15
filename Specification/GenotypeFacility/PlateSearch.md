
## Search for plates [ brapi/v2/plate-search ]

Search for plates in the database.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|Object containing MCPD data|Y|
|plates|list|list of plates|
|vendorProjectIdentifier|string||Y|
|vendorPlateIdentifier|string||Y|
|clientPlateIdentifier|string||Y|
|barcode|string||Y|
|plateFormat|string||Y|
|sampleType|string||Y|
|status|string||Y|
|samples|Object||Y|
|files|Object||Y|
|filename|string||Y|
|url|string||Y|
|md5sum|string||Y|
|filetype|string||Y|
|clientSampleIdentifiers|list||Y|

###  Search for plates [ brapi/v2/plate-search ] POST
+Request
	{
		"token" : "(required)",
		"vendorProjectIdentifier" : "(required)",
		"vendorPlateIdentifier" : "(optional)",
		"clientPlateIdentifier" : "(optional)",
		"sampleInfo": "true/false" (default:false),
	}
 
+Response:
	{
		"metadata":
		{   
			"status": [{"code": "",  "message" : "info message"}],
			"datafiles": []
   		},
   		"result" : { 
			"plates" :[
					{
						"vendorProjectIdentifier" : "(not null)", 
						"vendorPlateIdentifier" : "(not null)",
						"clientPlateIdentifier" : "(not null)",
	  					"vendorBarcode": "",
						"vendorBarcodeImageURL" : "",
						"plateFormat": "Plate_96" | "tubes",
						"sampleType" : "DNA" | "RNA" | "Tissue",
	   					"status": "(not null)",
						"statusTimestamp" : "2017-06-14 04:02:22 PST",
						"samples" : []
					}
				]
			"files" : [
					{
						"filename": "", 
						"URL" : "",
						"md5sum" : "",
						"fileType" : "fastq",
						"clientSampeIdentifiers" : [],
						"additionalInfo": {}
					}
				]
			}
		}
 	}
	
