#! /usr/bin/env python

import yaml
import sys
import json
import dereferenceAll
import os


def buildTermBrowserData():	
	if 'paths' in fullBrAPI:
		for path in fullBrAPI['paths']:
			for method in fullBrAPI['paths'][path]:
				pathStr = method + " " + path
				tag = fullBrAPI['paths'][path][method]['tags'][0]
				 
				if 'parameters' in fullBrAPI['paths'][path][method]:
					for param in fullBrAPI['paths'][path][method]['parameters']:
						parameterContent = dereferenceAll.dereferenceAll(param, fullBrAPI)
						if 'deprecated' not in parameterContent:
							addTerm(parameterContent['name'], parameterContent['description'], pathStr, tag, '', 'Query Parameter')
					
				if 'requestBody' in fullBrAPI['paths'][path][method]:
					requestContent = fullBrAPI['paths'][path][method]['requestBody']['content']
					if 'application/json' in requestContent and 'schema' in requestContent['application/json']:
						if path[:7] == '/search':
							collectTermsFromSchema(requestContent['application/json']['schema'], '', pathStr, tag, 'Search Request Parameter')
						else:
							collectTermsFromSchema(requestContent['application/json']['schema'], '', pathStr, tag, 'Data Field')
					
				if 'responses' in fullBrAPI['paths'][path][method]:
					if '200' in fullBrAPI['paths'][path][method]['responses']:
						responseContent = dereferenceAll.dereferenceAll(fullBrAPI['paths'][path][method]['responses']['200'], fullBrAPI)
						responseContent = responseContent['content']
						if 'application/json' in responseContent and 'schema' in responseContent['application/json']:
							collectTermsFromSchema(responseContent['application/json']['schema'], '', pathStr, tag, 'Data Field')
							
					if '202' in fullBrAPI['paths'][path][method]['responses']:
						responseContent = dereferenceAll.dereferenceAll(fullBrAPI['paths'][path][method]['responses']['202'], fullBrAPI)
						responseContent = responseContent['content']
						if 'application/json' in responseContent and 'schema' in responseContent['application/json']:
							collectTermsFromSchema(responseContent['application/json']['schema'], '', pathStr, tag, 'Data Field')
					

def collectTermsFromSchema(schema, className, pathStr, tag, type):
	schemaBody = dereferenceAll.dereferenceAll(schema, fullBrAPI)
	collectTermsRecursivly(schemaBody, className, pathStr, tag, type)


def collectTermsRecursivly(schemaBody, className, pathStr, tag, type):
	if 'x-brapi-metadata' in schemaBody and schemaBody['x-brapi-metadata']['primaryModel']:
		if 'title' in schemaBody['x-brapi-metadata']:
			className = schemaBody['x-brapi-metadata']['title']
			
			if 'description' in schemaBody['x-brapi-metadata']:
				addTerm(schemaBody['x-brapi-metadata']['title'], schemaBody['x-brapi-metadata']['description'], pathStr, tag, className, 'Class')
		
	
	if 'properties' in schemaBody:
		for termStr in schemaBody['properties']:
			if 'deprecated' not in schemaBody['properties'][termStr]:
				description = "No Description Found"
				if 'description' in schemaBody['properties'][termStr]:
					description = schemaBody['properties'][termStr]['description']
					
				addTerm(termStr, description, pathStr, tag, className, type)
							
				if 'properties' in schemaBody['properties'][termStr]:
					nextClassRef = ''
					if className != '':
						nextClassRef = className + '.' + termStr
					collectTermsRecursivly(schemaBody['properties'][termStr], nextClassRef, pathStr, tag, type)
						
				elif 'items' in schemaBody['properties'][termStr] and 'properties' in schemaBody['properties'][termStr]['items']:
					nextClassRef = ''
					if className != '':
						nextClassRef = className + '.' + termStr
					collectTermsRecursivly(schemaBody['properties'][termStr]['items'], nextClassRef, pathStr, tag, type)

	
def scanForPrimaryClassRef(schema):
	if type(schema) is dict:
		for fieldStr in schema:
			if(fieldStr == '$ref'):
				schemaBody = dereferenceAll.findRef(schema['$ref'], fullBrAPI)
				if 'x-brapi-metadata' in schemaBody:
					return schema['$ref']
			else:
				return scanForPrimaryClassRef(schema[fieldStr])
	elif type(schema) is list:
		for item in schema:
			scanForPrimaryClassRef(item)
			
	return ''


def addTerm(termStr, definitionStr, pathStr, tag, classRef, type):
	newDefinition = {
			'definition': definitionStr,
			'context':{
				'paths':[],
				'classes': [],
				'tags': [],
				'types': []
			}
		}
	
	termStr = termStr[0].lower() + termStr[1:]
	
	if termStr in terms:
		found = False
		for definition in terms[termStr]['definitions']:
			if definitionStr == definition['definition']:
				newDefinition = definition
				found = True
				break
		
		if not found:
			terms[termStr]['definitions'].append(newDefinition)
			newDefinition = terms[termStr]['definitions'][-1]
		
	else:
		term = {"definitions":[newDefinition]}
		terms[termStr] = term
		newDefinition = terms[termStr]['definitions'][0]
	
	newDefinition['context']['paths'] = appendContext(pathStr, newDefinition['context']['paths'])
	newDefinition['context']['classes'] = appendContext(classRef, newDefinition['context']['classes'])
	newDefinition['context']['tags'] = appendContext(tag, newDefinition['context']['tags'])
	newDefinition['context']['types'] = appendContext(type, newDefinition['context']['types'])
	 
		
def appendContext(value, array):
	if value != '':
		array.append(value)
		return list(set(array))
	return array

	
def printTermsToFile(outFilePath):
	fileName = outFilePath + 'brapi_glossary_terms.js'
	with open(fileName, 'w') as outfile:
		outfile.write('const rawWordList = ')
		json.dump(terms, outfile, indent=4, sort_keys=True)
		print("fileName - " + fileName)


def main():
	# # Path to BrAPI spec repo. Should end in /Specification/
	rootPath = '.'
	outFilePath = '.'
	if len(sys.argv) > 1:
		rootPath = sys.argv[1];
		
	if len(sys.argv) > 2:
		outFilePath = sys.argv[2];
	
	if rootPath[-1:] != '/':
		rootPath = rootPath + '/'
		
	if outFilePath[-1:] != '/':
		outFilePath = outFilePath + '/'
		
	with open(rootPath + 'brapi_openapi.yaml', "r") as stream:
		try:
			global fullBrAPI
			fullBrAPI = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			stream.close()
			
	buildTermBrowserData()
	printTermsToFile(outFilePath)


fullBrAPI = {}
terms = {}
main()
