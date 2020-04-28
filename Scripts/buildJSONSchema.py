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
	
	sortedPaths = sortPaths(parent)
	for pathObj in sortedPaths:
		path = pathObj['path']
		method = pathObj['method']
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
					secondTest['event'][0]['exec'] = getExecList(method, path, tagName.replace(' ', ''), '1')
					tag['item'].append(secondTest)
				break
	
	filename = outPath + 'collections/CompleteBrapiTest.' + versionNumber + '.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(collection, outfile, indent=4, sort_keys=True)

def sortPaths(parent):
	
	serverInfoPath = {}
	getPaths = []
	postPaths = []
	putPaths = []
	tablePaths = []
	vendorPaths = []
	searchPathPosts = []
	searchPathGets = []
			    
	if('paths' in parent):
		for path in parent['paths']:
			for method in parent['paths'][path]:
				pathObj = {'path': path, 'method': method}
				
				isServerInfoPath = re.fullmatch('^/serverinfo$', path)
				isBasePath = re.fullmatch('^/[a-z]+$', path)
				isBaseExtraPath = re.fullmatch('^/[a-z]+/[a-z]+$', path)
				isDbIdPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}$', path)
				isDbIdExtraPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}/[a-z]+$', path)
				isTablePath = re.fullmatch('^/[a-z]+/table$', path)
				isVendorPath = re.fullmatch('^/vendor/.+$', path)
				isSearchPath = re.fullmatch('^/search/[a-z]+(/{searchResultsDbId})?$', path)
			    
				dbid = mapPathToDbId(path)
					
				if isServerInfoPath:
					serverInfoPath = pathObj
				elif isVendorPath:
					vendorPaths.append(pathObj)
				elif isSearchPath:
					if method == 'get':
						vendorPaths.append(pathObj)
					elif method == 'post':
						vendorPaths.append(pathObj)
				elif isTablePath:
					tablePaths.append(pathObj)
				elif isBasePath or isBaseExtraPath or isDbIdPath or isDbIdExtraPath: 
					if method == 'get':
						getPaths.append(pathObj)
					elif method == 'post':
						postPaths.append(pathObj)
					elif method == 'put':
						putPaths.append(pathObj)
				else:
					print('missing pidgen hole for ' + method + path)
	
	sortedPaths = [serverInfoPath]
	sortedPaths.extend(getPaths)
	sortedPaths.extend(postPaths)
	sortedPaths.extend(putPaths)
	sortedPaths.extend(tablePaths)
	sortedPaths.extend(searchPathPosts)
	sortedPaths.extend(searchPathGets)
	sortedPaths.extend(vendorPaths)
	
	return sortedPaths
	

def getExecList(method, path, tag, variablePostfix='0'):
	execList = [
					"ContentType:application/json",
					"Schema:/" + versionNumber + "/metadata"
				]
	
	isServerInfoPath = re.fullmatch('^/serverinfo$', path)
	isSimpleListPath = re.fullmatch('^/commoncropnames$|^/studytypes$|^/observationlevels$|^/ontologies$|^/events$|^/markerpositions$', path)
	isBasePath = re.fullmatch('^/[a-z]+$', path)
	isBaseExtraPath = re.fullmatch('^/[a-z]+/[a-z]+$', path)
	isDbIdPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}$', path)
	isDbIdExtraPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}/[a-z]+$', path)
	isTablePath = re.fullmatch('^/[a-z]+/table$', path)
	isVendorPath = re.fullmatch('^/vendor/.+$', path)
	isSearchPath = re.fullmatch('^/search/[a-z]+(/{searchResultsDbId})?$', path)
    
	dbid = mapPathToDbId(path)
		
	
	if isSearchPath:
		execList.insert(0, "StatusCode:202,200:breakiffalse")
		execList.append("SearchSchema:/" + versionNumber + "/" + tag + '/' + buildResponseObjectName(method, path) + ':' + getSearchPathVariableName(path))
	else:
		execList.insert(0, "StatusCode:200:breakiffalse")
		execList.append("Schema:/" + versionNumber + "/" + tag + '/' + buildResponseObjectName(method, path))
		if isServerInfoPath:
			execList.append('SaveCalls:V2')
		elif isSimpleListPath:
			True
		elif isVendorPath:
			if method == 'get':
				True
			elif method == 'post':
				True
		elif isTablePath:
				True
		elif isBaseExtraPath:
				True
		elif isBasePath: 
			if method == 'get':
				execList.append('GetValue:/result/data/0/' + dbid + ':' + dbid +'0')
				execList.append('GetValue:/result/data/1/' + dbid + ':' + dbid +'1')
			elif method == 'post':
				True
			elif method == 'put':
				True
		elif isDbIdPath:
			if method == 'get':
				execList.append('IsEqual:/result/' + dbid + ':' + dbid + variablePostfix)
			elif method == 'put':
				execList.append('IsEqual:/result/' + dbid + ':' + dbid + variablePostfix)
		elif isDbIdExtraPath:
			if method == 'get':
				True
			elif method == 'post':
				True
			elif method == 'put':
				True
		else:
			print('missing exec list for ' + method + path)		
	return execList

def mapPathToDbId(path):
	## Special cases because English is difficult
	if path.startswith('/attributevalues'):
			return 'attributeValueDbId'
	elif path.startswith('/breedingmethods'):
			return 'breedingMethodDbId'
	elif path.startswith('/callsets'):
			return 'callSetDbId'
	elif path.startswith('/crosses'):
			return 'crossDbId'
	elif path.startswith('/plannedcrosses'):
			return 'plannedCrossDbId'
	elif path.startswith('/crossingprojects'):
			return 'crossingProjectDbId'
	elif path.startswith('/observationunits'):
			return 'observationUnitDbId'
	elif path.startswith('/people'):
			return 'personDbId'
	elif path.startswith('/referencesets'):
			return 'referenceSetDbId'
	elif path.startswith('/seedlots'):
			return 'seedLotDbId'
	elif path.startswith('/studies'):
			return 'studyDbId'
	elif path.startswith('/variables'):
			return 'observationVariableDbId'
	elif path.startswith('/variantsets'):
			return 'variantSetDbId'
	else:
		rootPath = path.split('/')[1]		
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
	isSearchPath = re.fullmatch('^/search/[a-z]+(/{searchResultsDbId})?$', path)
	paramsList = []
	if isSearchPath:
		if method.lower() == 'post':
			param = {'param': 'json', 'value': '{}'}
			paramsList.append(param)
	else:
		if method.lower() == 'post':
			param = {'param': 'json', 'value': '[{}]'}
			paramsList.append(param)
		elif method.lower() == 'put':
			param = {'param': 'json', 'value': '{}'}
			paramsList.append(param)
	return paramsList
	
def buildResponseObjectName(method, path, responseCode = '200'):
	pathParts = path.split('/')
	name = method
	for pathPart in pathParts:
		name = name + pathPart.replace('{', '').replace('}', '').capitalize()
	name = name + 'Response'
	if responseCode != '200':
		name = name + responseCode
	return name 

def isNotDeprecated(obj):
	if 'deprecated' in obj:
		return not obj['deprecated']
	return True
	

def buildJSONSchemas(method, path, tag, parent):
	for responseCode in parent['paths'][path][method]['responses']:
		if not responseCode.startswith('4'):
			schema = parent['paths'][path][method]['responses'][responseCode]['content']['application/json']['schema']['properties']['result']
		
			schema = fixSchema(schema)
			schemaObj = {
							"$schema": "http://json-schema.org/draft-04/schema#",
							"title": buildResponseObjectName(method, path, responseCode),
							"type": "object",
							"properties": {
								"result": schema
							},
							"required": [
								"result"
							]
						}
			
			filename = outPath + 'schemas/' + versionNumber + '/' + tag + '/' + buildResponseObjectName(method, path, responseCode) + '.json'
			os.makedirs(os.path.dirname(filename), exist_ok=True)
			with open(filename, 'w') as outfile:
				json.dump(schemaObj, outfile, indent=4, sort_keys=True)
								
							

def fixSchema(schema):
	if 'data' in schema['properties']:
		schema['properties']['data']['minItems'] = 1
		
	schema = removeDeprecated(schema)
	schema = removeSwaggerTerms(schema)
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

def removeSwaggerTerms(parent):
	newParent = deepcopy(parent)
	if type(newParent) is dict:
		if 'example' in newParent:
			newParent.pop('example')
		if 'discriminator' in newParent:
			newParent.pop('discriminator')
		for childKey in newParent:
			newParent[childKey] = removeSwaggerTerms(newParent[childKey])
	elif type(newParent) is list:
		newList = []
		for item in newParent:
			newList.append(removeSwaggerTerms(item))
		newParent = newList
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
					if 'enum' in fieldObj:
						newParent['properties'][fieldName]['enum'].append(None)
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
	
	filename = outPath + 'schemas/' + versionNumber + '/metadata.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(schemaObj, outfile, indent=4, sort_keys=True)
	
	
outPath = './out/'
yamlPath = './brapi_openapi.yaml'
versionNumber = 'vX.X'
verbose = False

verbose = '-v' in sys.argv 

if '-version' in sys.argv:
	vi = sys.argv.index('-version')
	versionNumber = sys.argv[vi + 1]
	
if '-brapi' in sys.argv:
	bi = sys.argv.index('-brapi')
	yamlPath = sys.argv[bi + 1]

if '-out' in sys.argv:
	ri = sys.argv.index('-out')
	outPath = sys.argv[ri + 1]
if outPath[-1] != '/':
	outPath = outPath + '/'

parentFile = dereferenceAll.dereferenceBrAPI(filePath = yamlPath)

buildCollection(parentFile)
buildMetaData(parentFile)
	
