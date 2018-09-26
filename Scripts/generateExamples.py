#! /usr/bin/env python

import yaml
import glob
import sys
import json
from copy import deepcopy

def buildMetaData(includePagination):
	example = {'datafiles': [], 'status': [], 'pagination': {}}
	if includePagination :
		example['pagination'] = {'currentPage': 0, 'pageSize': 1000, 'totalCount': 2, 'totalPages': 1}
	return example

def buildStringExample(fieldName, strSchema, index = 0):
	strExample = fieldName + str(index)
	if('enum' in strSchema):
		strExample = strSchema['enum'][index]
	elif('format' in strSchema):
		if 'date' == strSchema['format']:
			strExample = '2018-01-01'
		elif 'date-time' == strSchema['format']:
			strExample = '2018-01-01T14:47:23-0600'
	return strExample

def buildIntExample(fieldName):
	return 0

def buildArrayExample(fieldName, itemSchema):
	arr = []
	
	if ('type' in itemSchema):
		if (itemSchema['type'] == 'string'):
			arr.append(buildStringExample(fieldName, itemSchema, 0))
			arr.append(buildStringExample(fieldName, itemSchema, 1))
		elif (itemSchema['type'] == 'int'):
			arr = [1, 2]
		elif (itemSchema['type'] == 'array'):
			arr.append(buildArrayExample(fieldName, itemSchema['items']))
			arr.append(buildArrayExample(fieldName, itemSchema['items']))
		elif (itemSchema['type'] == 'object'):
			arr.append(buildObjectExample(itemSchema, 0))
			arr.append(buildObjectExample(itemSchema, 1))
	elif ('properties' in itemSchema):
		arr.append(buildObjectExample(itemSchema, 0))
		arr.append(buildObjectExample(itemSchema, 1))
		
	return arr

def buildObjectExample(schema, index = 0):
	example = {}
	
	if ('properties' in schema):
		for fieldName in schema['properties']:
			if(fieldName == 'metadata'):
				example['metadata'] = buildMetaData('data' in schema['properties']['result']['properties'])
			else:
				fieldObj = schema['properties'][fieldName]
				
				if ('type' in fieldObj):
					if (fieldObj['type'] == 'string'):
						example[fieldName] = buildStringExample(fieldName, fieldObj, index)
					elif (fieldObj['type'] == 'integer'):
						example[fieldName] = buildIntExample(fieldName)
					elif (fieldObj['type'] == 'array'):
						example[fieldName] = buildArrayExample(fieldName, fieldObj['items'])
					elif (fieldObj['type'] == 'object'):
						example[fieldName] = buildObjectExample(fieldObj)
				elif ('properties' in fieldObj):
					example[fieldName] = buildObjectExample(fieldObj)
			
	return example

def addExamples(obj):
	if('paths' in obj):
		for path in obj['paths']:
			for method in obj['paths'][path]:
				for responseCode in obj['paths'][path][method]['responses']:
					response = obj['paths'][path][method]['responses'][responseCode]
					if ('schema' in response):
						schema = dereferenceAll(deepcopy(response['schema']))
						newExample = buildObjectExample(schema)
						obj['paths'][path][method]['responses'][responseCode]['examples']['application/json'] = newExample
						
	return obj

def dereferenceAll(obj, modelsPath = 'C:/Users/ps664/Documents/BrAPI/API/Specification/ModelDefinitions/'):
	if type(obj) is dict:
		for fieldStr in obj:
			if(fieldStr == '$ref'):
				refName = obj[fieldStr].split('/')[2]
				path = modelsPath + refName + '.yaml'
				refObj = dereferenceAll(readFileToDict(path)['definitions'][refName])
				obj = {**obj, **refObj}
			else:
				obj[fieldStr] = dereferenceAll(obj[fieldStr])
		if '$ref' in obj:
			obj.pop('$ref')
	elif type(obj) is list:
		newList = []
		for item in obj:
			newList.append(dereferenceAll(item))
		obj = newList
		
	#print(obj)
	return obj


def readFileToDict(path):
	fileObj = {}	
	with open(path, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			print(exc)
	return fileObj


rootPath = './'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

if(rootPath[-1] == '/'):
	rootPath = rootPath + '**/*.yaml'

for filename in glob.iglob(rootPath, recursive=True):
	print(filename)
	file = readFileToDict(filename)	
	newFile = addExamples(file)
	
	with open(filename, 'w') as outfile:
		yaml.dump(newFile, outfile, default_flow_style=False, width=float("inf"))
	
		

	
