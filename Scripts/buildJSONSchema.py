#! /usr/bin/env python

import yaml
import glob
import sys
import json
import re
import os
from copy import deepcopy
import dereferenceAll

varRegex = re.compile('\{(.*)\}')

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
						tag['item'].append(
							{
								"name": method + path,
								"endpoint": path,
								"description": parent['paths'][path][method]['description'],
								"requires": getRequiresList(method, path),
								"request": {
									"url": "{baseurl}" + path,
									"method": method.upper()
								},
								"event": [
									{
										"listen": "test",
										"type": "text/plain",
										"exec": getExecList(method, path, tagName.replace(' ', ''))
									}
								]
							}
							)
				
	with open(rootPath + 'collections/CompleteBrapiTest.v1.3.json', 'w') as outfile:
		json.dump(collection, outfile, indent=4, sort_keys=True)
		
def getExecList(method, path, tag):
	execList = [
					"StatusCode:200:breakiffalse",
					"ContentType:application/json",
					"Schema:/v1.3/metadata",
					"Schema:/v1.3/" + tag + '/' + buildResponseObjectName(method, path)
				]
	if path == '/calls':
		execList.append('SaveCalls')
	return execList

def getRequiresList(method, path):
	requiresList = []
	if '{' in path:
		requiresList.append(varRegex.search(path).group(1))
	return requiresList
	
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
	
