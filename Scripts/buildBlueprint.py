#! /usr/bin/env python

import sys
import json

def go():
	
	# Tedious to write out the names of all the directories and files but this let's us control the order of assembly
	sources=[  "GeneralInfo/Intro.md",
		       "GeneralInfo/URL_Structure.md",
		       "GeneralInfo/Response_Structure.md",
		       "GeneralInfo/Error_Handling.md",
		       "GeneralInfo/Date_Time_Encoding.md",
		       "GeneralInfo/Location_Encoding.md",
		       "GeneralInfo/Search_Services.md",
		       "GeneralInfo/Asychronous_Processing.md",
		       "Authentication/README.md" ,
		       "Calls/README.md" ,
		       "Crops/README.md",
		       "Germplasm/README.md",
		       "GermplasmAttributes/README.md",
		       "Programs/README.md",
		       "Trials/README.md",
		       "Studies/README.md",
		       "Locations/README.md",
		       "Phenotypes/README.md",
		       "ObservationVariables/README.md",
		       "Images/README.md",
		       "GenomeMaps/README.md",
		       "Markers/README.md",
		       "MarkerProfiles/README.md",
		       "Samples/README.md",
		       "VendorSamples/README.md",
		       "Lists/README.md",
		       "People/README.md"
		       ]
	
	rootPath = '.'
	if len(sys.argv) > 1 :
	    rootPath = sys.argv[1]
	
	fullText = ''
	for source in sources:
		filename = rootPath + '/Specification/' + source
		with open(filename, "r") as inFile:
			fullText += inFile.read()
	
	outFilePath = rootPath + '/brapi_blueprint.apib'
	with open(outFilePath, "w") as outFile:
		outFile.write(fullText)
		print(outFilePath)
		
	outFileJsonPath = rootPath + '/brapi_blueprint.apib.json'
	with open(outFileJsonPath, "w") as outFileJson:
		jsonWrapper = {'code': fullText}
		json.dump(jsonWrapper, outFileJson)
		print(outFileJsonPath)
			
			
			
go()