#! /usr/bin/env python

import yaml
import glob
import sys
import json
import re
import os
from copy import deepcopy
import dereferenceAll

def buildJSONSchemas(parent, verbose):
	
	if 'schemas' in parent['components']:
		for schemaName in parent['components']['schemas']:
			if verbose:
				print('Data model: ' + schemaName)
			title = schemaName
			schema = parent['components']['schemas'][schemaName]
			module = ''
			if 'x-brapi-metadata' in schema:
				if 'primaryModel' in schema['x-brapi-metadata'] and schema['x-brapi-metadata']['primaryModel']:
					if verbose:
						print('-- Added')
					if 'title' in schema['x-brapi-metadata']:
						title = schema['x-brapi-metadata']['title']
					if 'module' in schema['x-brapi-metadata']:
						module = schema['x-brapi-metadata']['module']
					buildJSONSchema(schema, title, module, verbose)
					
				else:
					if verbose:
						print('-- Skipped')
						
	else:
		print("Error: no schemas found")


def buildJSONSchema(schema, title, module, verbose):		
	schema = fixSchema(schema)
	schemaObj = {
				"$schema": "http://json-schema.org/draft/2020-12/schema",
				"$id": "https://brapi.org/Specification/BrAPI-Schema/" + module + "/" + title +".json",
				"$defs": {
					title : {
						"title": title,
						"type": "object",
					    "properties": schema["properties"]
					}
				}
			}
	
	if 'required' in schema:
		schemaObj['$defs'][title]['required'] = schema['required']
			
	filename = outPath + module + '/' + title + '.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w') as outfile:
		json.dump(schemaObj, outfile, indent=4, sort_keys=True)
								
							

def fixSchema(schema):
	schema = addMinItems(schema)
	schema = removeDeprecated(schema)
	schema = removeSwaggerTerms(schema)
	schema = fixStringFormats(schema)
	schema = allowNullFields(schema)
	schema = addRequired(schema)
	schema = addRefs(schema)
	return schema

def addRefs(parent):
	newParent = deepcopy(parent)
	if type(parent) is dict:
		if 'properties' in newParent:
			className = ''
			if 'x-brapi-metadata' in newParent:
				className = newParent['x-brapi-metadata']['title']
			for term in parent['properties']:
				if term.endswith('DbId') and (term.casefold() != (className + 'DbId').casefold()):
					oldTermDetails = newParent['properties'].pop(term)
					newTerm = term[:-4]
					newTermTitle = newTerm[0].upper() + newTerm[1:]
					if newTerm + 'Name' in newParent['properties']:
						newParent['properties'].pop(newTerm + 'Name')
					newParent['properties'][newTerm] = { '$ref': newTermTitle + '.json#/$defs/' + newTermTitle, 'description': oldTermDetails['description'], 'relationshipType': 'EDITME-to-one', 'referencedAttribute': className[0].lower() + className[1:] + 's' }
				elif term.endswith('DbIds') and (term.casefold() != (className + 'DbIds').casefold()):
					oldTermDetails = newParent['properties'].pop(term)
					newTerm = term[:-5]
					newTermTitle = newTerm[0].upper() + newTerm[1:]
					newParent['properties'][newTerm + 's'] = { 'items':{ '$ref': newTermTitle + '.json#/$defs/' + newTermTitle }, 'type': 'array', 'description': oldTermDetails['description'], 'relationshipType': 'EDITME-to-many', 'referencedAttribute': className[0].lower() + className[1:] + 's' }
	
	return newParent

def addMinItems(parent):
	newParent = deepcopy(parent)
	if 'data' in newParent['properties']:
		newParent['properties']['data']['minItems'] = 1
	return newParent	
	
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

def addRequired(parent):
	newParent = deepcopy(parent)
	if type(newParent) is dict:
		if 'properties' in newParent:
			newParent['required'] = list(newParent['properties'].keys());
		for childKey in newParent:
			newParent[childKey] = addRequired(newParent[childKey])

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
	
	
outPath = './out/'
yamlPath = './brapi_openapi.yaml'
verbose = False

verbose = '-v' in sys.argv 
	
if '-brapi' in sys.argv:
	bi = sys.argv.index('-brapi')
	yamlPath = sys.argv[bi + 1]

if '-out' in sys.argv:
	ri = sys.argv.index('-out')
	outPath = sys.argv[ri + 1]
	
if outPath[-1] != '/':
	outPath = outPath + '/'

if verbose:
	print('input YAML file: ' + yamlPath)
	print('output directory: ' + outPath)
	
parentFile = dereferenceAll.dereferenceBrAPI(yamlPath, verbose)

buildJSONSchemas(parentFile, verbose)
