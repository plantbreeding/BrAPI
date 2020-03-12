#! /usr/bin/env python

import yaml
import glob
import sys
import json
import re
import os
from copy import deepcopy
import dereferenceAll

varRegex = re.compile('\{([^\{\}]*)\}')
secondTestRegex = re.compile('^\/\w+\/\{\w+\}$')

def buildCollection(parent):
	collection = {
					"info": {
						"name": "Complete BrAPI test",
						"description": "Includes all resources, schema and data",
						"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
					},
					"item": []
				}
	
	if('tags' in parent):
		for tagObj in parent['tags']:
			if tagObj['name'] != 'Search Services':
				collection['item'].append(
									{
									"name": tagObj['name'],
									"description": tagObj['description'],
									"item": []
									} 
									)
	
	if('paths' in parent):
		for path in parent['paths']:
			for method in parent['paths'][path]:
				for tag in collection['item']:
					tagName = tag['name']
					if tagName in parent['paths'][path][method]['tags'] and isNotDeprecated(parent['paths'][path][method]):	
						
						buildJSONSchemas(method, path, tagName.replace(' ', ''), parent)
						newTest = {
									"name": method.upper() + ' ' + path,
									"endpoint": path,
									"description": parent['paths'][path][method]['description'],
									"requires": getRequiresList(method, path),
									"request": {
										"url": "{baseurl}" + replacePathParams(method, path),
										"method": method.upper()
									},
									"event": [
										{
											"listen": "test",
											"type": "text/plain",
											"exec": getExecList(method, path, tagName.replace(' ', ''))
										}
									],
									"parameters": getParamsList(method, path)
								}
							
						tag['item'].append(newTest)
						
						if method.lower() == 'get' and secondTestRegex.match(path):
							secondTest = deepcopy(newTest)
							secondTest['name'] += ' with second DbId' 
							secondTest['requires'] = getRequiresList(method, path, '1')
							secondTest['request']['url'] = "{baseurl}" + replacePathParams(method, path, '1')
							tag['item'].append(secondTest)
						break
	
	filename = rootPath + 'collections/CompleteBrapiTest.' + versionNumber + '.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(collection, outfile, indent=4, sort_keys=True)
		
def getExecList(method, path, tag):
	execList = [
					"StatusCode:200:breakiffalse",
					"ContentType:application/json",
					"Schema:/" + versionNumber + "/metadata",
					"Schema:/" + versionNumber + "/" + tag + '/' + buildResponseObjectName(method, path)
				]
	
	isBasePath = re.match('^/[a-z]+$', path)
	isDbIdPath = re.match('^/[a-z]+/\{$[a-zA-Z]+}', path)
	isVendorPath = re.match('^/vendor/.+$', path)
	isSearchPostPath = re.match('^/search/[a-z]+$', path)
	isSearchGetPath = re.match('^/search/[a-z]+/{searchResultsDbId}$', path)
	if method.lower() == 'get':
		if path == '/calls':
			execList.append('SaveCalls')
		else:
			dbid = mapPathToDbId(path)
			execList.append('GetValue:/result/data/0/' + dbid + ':' + dbid +'0')
			execList.append('GetValue:/result/data/1/' + dbid + ':' + dbid +'1')
		
	if '/search' in path and method.lower() == 'post':
			varName = path.split('/')[2] + 'SearchResultDbId'
			execList.append('GetValue:/result/searchResultDbId:' + varName)
			
			
	return execList

def mapPathToDbId(path):
	## Special cases because English is difficult
	if path == '/attributevalues':
			return 'attributeValueDbId'
	elif path == '/breedingmethods':
			return 'breedingMethodDbId'
	elif path == '/callsets':
			return 'callSetDbId'
	elif path == '/crossingprojects':
			return 'crossingProjectDbId'
	elif path == '/observationunits':
			return 'observationUnitDbId'
	elif path == '/people':
			return 'personDbId'
	elif path == '/referencesets':
			return 'referenceSetDbId'
	elif path == '/seedlots':
			return 'seedLotDbId'
	elif path == '/studies':
			return 'studyDbId'
	elif path == '/variables':
			return 'observationVariableDbId'
	elif path == '/variantsets':
			return 'variantSetDbId'
	else:
		rootPath = path[1:]		
		if rootPath[-1] == 's':
			rootPath = rootPath[:-1]
		return rootPath + 'DbId'		

def getRequiresList(method, path, varPostfix = '0'):
	requiresList = []
	if '{' in path:
		if '/search' in path and method.lower() == 'get':
			requiresList.append(getSearchPathVariableName(path))
		else:
			for var in varRegex.findall(path):
				requiresList.append(var + varPostfix)
	return requiresList

def replacePathParams(method, path, varPostfix = '0'):
	newPath = path
	if '{' in path:
		if '/search' in path and method.lower() == 'get':
			newPath = varRegex.sub('{' + getSearchPathVariableName(path) + '}', path)
		else:
			newPath = varRegex.sub('{\g<1>' + varPostfix + '}', path)
	return newPath

def getSearchPathVariableName(path):
	return path.split('/')[2] + 'SearchResultDbId'

def getParamsList(method, path):
	paramsList = []
	return paramsList
	
def buildResponseObjectName(method, path):
	pathParts = path.split('/')
	name = method
	for pathPart in pathParts:
		name = name + pathPart.replace('{', '').replace('}', '').capitalize()
	return name + 'Response'

def isNotDeprecated(obj):
	if 'deprecated' in obj:
		return not obj['deprecated']
	return True
	

def buildJSONSchemas(method, path, tag, parent):
	schema = {}
	try:
		schema = parent['paths'][path][method]['responses']['200']['content']['application/json']['schema']['properties']['result']
	except:
		print('schema not found')
	
	schema = fixSchema(schema)
	schemaObj = {
					"$schema": "http://json-schema.org/draft-04/schema#",
					"title": buildResponseObjectName(method, path),
					"type": "object",
					"properties": {
						"result": schema
					},
					"required": [
						"result"
					]
				}
	
	filename = rootPath + 'schemas/' + versionNumber + '/' + tag + '/' + buildResponseObjectName(method, path) + '.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(schemaObj, outfile, indent=4, sort_keys=True)
								
							

def fixSchema(schema):
	if 'data' in schema['properties']:
		schema['properties']['data']['minItems'] = 1
		
	schema = removeDeprecated(schema)
	schema = fixStringFormats(schema)
	schema = allowNullFields(schema)
	return schema

def removeDeprecated(parent):
	newParent = deepcopy(parent)
	if type(parent) is dict:
		for childKey in parent:
			child = parent[childKey]
			if type(child) is dict:
				if 'deprecated' in child and child['deprecated']:
					newParent.pop(childKey)
				else:
					newParent[childKey] = removeDeprecated(child)
	return newParent

def fixStringFormats(parent):
	newParent = deepcopy(parent)
	if type(parent) is dict:
		for childKey in parent:
			child = parent[childKey]
			if type(child) is dict:
				if 'format' in child and 'type' in child:
					if child['format'] != 'date-time' and child['format'] != 'uri':
						newParent[childKey].pop('format')
				else:
					newParent[childKey] = fixStringFormats(child)
	return newParent

def allowNullFields(parent):
	newParent = deepcopy(parent)
	if type(parent) is dict:
		if 'properties' in parent:
			
			requiredFields = []
			if 'required' in parent:
				requiredFields = parent['required']
				
			for fieldName in parent['properties']:
				fieldObj = parent['properties'][fieldName]
				newParent['properties'][fieldName] = allowNullFields(fieldObj)
				
				if not fieldName in requiredFields:
					types = ['null']
					if 'type' in fieldObj:
						types.append(fieldObj['type'])
					newParent['properties'][fieldName]['type'] = types
		else:
			for fieldName in parent:
				if type(parent[fieldName]) is dict:
					newParent[fieldName] = allowNullFields(parent[fieldName])
			
				
	return newParent
			
def buildMetaData(parent):
	metaSchema = fixSchema(parent['components']['schemas']['metadata'])
	schemaObj = {
					"$schema": "http://json-schema.org/draft-04/schema#",
					"title": "metadata",
					"type": "object",
					"properties": {
						"metadata": metaSchema
					},
					"required": [
						"metadata"
					]
				}
	
	filename = rootPath + 'schemas/' + versionNumber + '/metadata.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(schemaObj, outfile, indent=4, sort_keys=True)
	
	
rootPath = './out/'
versionNumber = 'vX.X'
verbose = False

verbose = '-v' in sys.argv 

if '-version' in sys.argv:
	vi = sys.argv.index('-version')
	versionNumber = sys.argv[vi + 1]

if '-root' in sys.argv:
	ri = sys.argv.index('-root')
	rootPath = sys.argv[ri + 1]
if rootPath[-1] != '/':
	rootPath = rootPath + '/'

parentFile = dereferenceAll.dereferenceBrAPI(filePath = rootPath + 'brapi_openapi.yaml')

buildCollection(parentFile)
buildMetaData(parentFile)
	
