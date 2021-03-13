#! /usr/bin/env python

import yaml
import sys
import json
import dereferenceAll
import os

def buildTermBrowserData(specPath):
	with open(specPath + '/brapi_openapi.yaml', "r") as stream:
		try:
			fullBrAPI = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			stream.close()
	##fullBrAPI = dereferenceAll.dereferenceBrAPI(filePath = rootPath + '/brapi_openapi.yaml')

	collection = {}
	
	## Find service grouping Tags
	if('tags' in fullBrAPI):
		for tagObj in fullBrAPI['tags']:
			if tagObj['name'] != 'Search Services':
				collection[tagObj['name']] = {'Calls': {}, 'Datatypes': {}}

	paths = fullBrAPI['paths']
	if('paths' in fullBrAPI):
		for path in fullBrAPI['paths']:
			for method in fullBrAPI['paths'][path]:
				for tag in collection:
					if tag in fullBrAPI['paths'][path][method]['tags']:
						if path not in collection[tag]['Calls']:
							collection[tag]['Calls'][path] = {}
						
						## Add path contents to the Calls section
						collection[tag]['Calls'][path].update({'methods' : fullBrAPI['paths'][path]})
						
						## Add the request body object to the Datatypes section, if applicable 
						if 'requestBody' in fullBrAPI['paths'][path][method]:
							requestContent = fullBrAPI['paths'][path][method]['requestBody']['content']
							requestSchema = {}
							if 'application/json' in requestContent and '$ref' in requestContent['application/json']['schema']:
								schemaName = requestContent['application/json']['schema']['$ref'].split('/')[-1:][0]
								schemaBody = dereferenceAll.dereferenceAll(requestContent['application/json']['schema'], fullBrAPI)
								requestSchema = {schemaName: schemaBody}
							collection[tag]['Datatypes'].update(requestSchema)
						
						
						## Find the base response object, ignore metadata etc
						if '$ref' in fullBrAPI['paths'][path][method]['responses']['200']:
							responseHolderRef = fullBrAPI['paths'][path][method]['responses']['200']['$ref']
							responseHolder = dereferenceAll.findRef(responseHolderRef, fullBrAPI)
						else:
							responseHolder = fullBrAPI['paths'][path][method]['responses']['200']
						
						
						## Add the response body object to the Datatypes section
						responseSchema = {}
						responseResult = responseHolder['content']['application/json']['schema']['properties']['result']
						if '$ref' in responseResult:
							schemaName = responseResult['$ref'].split('/')[-1:][0]
							schemaBody = dereferenceAll.dereferenceAll(responseResult, fullBrAPI)
							responseSchema = {schemaName: schemaBody}
						elif 'properties' in responseResult and 'data' in responseResult['properties'] and '$ref' in responseResult['properties']['data']['items']:
							schemaName = responseResult['properties']['data']['items']['$ref'].split('/')[-1:][0]
							schemaBody = dereferenceAll.dereferenceAll(responseResult['properties']['data']['items'], fullBrAPI)
							responseSchema = {schemaName: schemaBody}
						
						collection[tag]['Datatypes'].update(responseSchema)
							
	return collection					

def buildTermBrowserDataFile(specPath):
	fileContent = {}
	## For each BrAPI Module
	for module in next(os.walk(specPath))[1]:
		if module[:5] == 'BrAPI':
			print(specPath + module + '/')
			moduleObj = buildTermBrowserData(specPath + module + '/')
			fileContent.update({module: moduleObj})
	
	fileName = specPath + '/TermBrowser.json'
	with open(fileName, 'w') as outfile:
		json.dump(fileContent, outfile, indent=4, sort_keys=True)
		print("fileName - " + fileName)

## Path to BrAPI spec repo. Should end in /Specification/
rootPath = '.'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

if rootPath[-1:] != '/':
	rootPath = rootPath + '/'

buildTermBrowserDataFile(rootPath)
