## Plate Details by vendorPlateId [ /brapi/v2/plate/{id} ] 
Scope: Genotyping facilty. Status: Proposed for V2.

##### Response data types

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|Oobject|Object containing MCPD data|Y|
|vendorProjectIdentifier|string|the name or identifier given to a project by the vendor|Y|
|vendorPlateIdentifier|string|the name or identifier of the plate, given by the vendor|Y|
|clientPlateIdentifier|string|the name of the plate, given by the client|Y|
|barcode|string|a string that can be represented as a barcode, identifying this plate|N|
|plateFormat|string|defines that plate format, usually Plate_96 or tubes for plateless format|Y|
|sampleType|string|DNA or RNA or Tissue, etc.|Y|
|status|string|The status of the plate in the processing pipeline. Typically,  "Received", "Processing", "QC_passed", QC_failed", "Completed" (as per vendor-requirements call)|Y|
|samples|Array|list of samples in the plate|Y|
||||
||||
||||
||||
 

### Plate Details by vendorPlateId [ /brapi/v2/plate/{id} ] GET
+ Parameters
 	+ id (required, string, `8338`)

+ Response 200 (application/json)

	{
		"metadata":{   
			"status": [{"code": "",  "message" : "info message"}],
		"datafiles": []
	},
	"result" : {
		"vendorProjectIdentifier" : "(not null)", 
		"vendorPlateIdentifier" : "(not null)",
		"clientPlateIdentifier" : "(not null)",
		"barcode" : "",
		"plateFormat" : "Plate_96" | "tubes",
		"sampleType" : "DNA" | "RNA" | "Tissue",
		"status" :  "(not null)",
		"statusTimeStamp" : "2017-06-01 01:57 GMT", #define this standard
		"samples" :[]
	}
 
## Delete individual plate  [ /brapi/v2/plate/{id} ] DELETE
+ Parameters
 	+ id (required, string, `8338`)
	+ token (required, string, 'skdkd')

+ Response 200 (application/json)
 
	{
		"metadata":{   
       			"status": [{"code": "",  "message" : "info message"}],
			"datafiles": []
	},
	"result" : { 
	}

