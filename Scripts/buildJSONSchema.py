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
	
	filename = rootPath + 'collections/CompleteBrapiTest.v1.3.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(collection, outfile, indent=4, sort_keys=True)
		
def getExecList(method, path, tag):
	execList = [
					"StatusCode:200:breakiffalse",
					"ContentType:application/json",
					"Schema:/v1.3/metadata",
					"Schema:/v1.3/" + tag + '/' + buildResponseObjectName(method, path)
				]
	if method.lower() == 'get':
		if path == '/calls':
			execList.append('SaveCalls')
		elif path[1:-1] in ['program', 'location', 'trial', 'method', 'scale', 'trait', 'marker', 'map', 'sample', 'list', 'image']:
			execList.append('GetValue:/result/data/0/' + path[1:-1] + 'DbId:' + path[1:-1] +'DbId0')
			execList.append('GetValue:/result/data/1/' + path[1:-1] + 'DbId:' + path[1:-1] +'DbId1')
		elif path == '/studies':
			execList.append('GetValue:/result/data/0/studyDbId:studyDbId0')
			execList.append('GetValue:/result/data/1/studyDbId:studyDbId1')
		elif path == '/germplasm':
			execList.append('GetValue:/result/data/0/germplasmDbId:germplasmDbId0')
			execList.append('GetValue:/result/data/1/germplasmDbId:germplasmDbId1')
		elif path == '/breedingmethods':
			execList.append('GetValue:/result/data/0/breedingMethodDbId:breedingMethodDbId0')
			execList.append('GetValue:/result/data/1/breedingMethodDbId:breedingMethodDbId1')
		elif path == '/markerprofiles':
			execList.append('GetValue:/result/data/0/markerProfileDbId:markerProfileDbId0')
			execList.append('GetValue:/result/data/1/markerProfileDbId:markerProfileDbId1')
		elif path == '/people':
			execList.append('GetValue:/result/data/0/personDbId:personDbId0')
			execList.append('GetValue:/result/data/1/personDbId:personDbId1')
		elif path == '/variables':
			execList.append('GetValue:/result/data/0/observationVariableDbId:observationVariableDbId0')
			execList.append('GetValue:/result/data/1/observationVariableDbId:observationVariableDbId1')
		elif path == '/maps/{mapDbId}':
			execList.append('GetValue:/result/data/0/linkageGroupName:linkageGroupName0')
		
	if '/search' in path and method.lower() == 'post':
			varName = path.split('/')[2] + 'SearchResultDbId'
			execList.append('GetValue:/result/searchResultDbId:' + varName)
			
			
	return execList

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
	
	filename = rootPath + 'schemas/v1.3/' + tag + '/' + buildResponseObjectName(method, path) + '.json'
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
	
	filename = rootPath + 'schemas/v1.3/metadata.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(schemaObj, outfile, indent=4, sort_keys=True)
	
	
rootPath = './out/'
verbose = False

if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
	if rootPath[-1] != '/':
		rootPath = rootPath + '/'
if len(sys.argv) > 2 :
	verbose = sys.argv[2] == '-v';
	
parentFile = dereferenceAll.dereferenceBrAPI()

buildCollection(parentFile)
buildMetaData(parentFile)
	
