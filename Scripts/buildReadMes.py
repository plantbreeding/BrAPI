#! /usr/bin/env python

import yaml
import glob
import sys
import json
import derefernceAll
##import buildOpenAPI
import generateExamples


def buildTitleStr(path, method = 'GET', params = [], deprecated = False):

	titleStr = '\n\n### ' 
	if deprecated:
		titleStr += '**Deprecated** '
	titleStr += method.capitalize() + ' '
		
	pathPieces = path.split('/')
	objects = ''
	keys = ''
	for piece in pathPieces[1:]:
		if piece[0] == '{' :
			word = ''
			if keys == '':
				word += 'by '
			else:
				word += 'and '
			word += piece[1:-1] + ' '
			keys += word
		else:
			objects += piece[0].upper() + piece[1:] + ' '
	titleStr += objects
	titleStr += keys
	
	titleStr += ' [' + method.upper() + ' /brapi/v1' + path
	
	for param in params:
		if param['in'] == 'query' :
		    titleStr += '{?' + param['name'] + '}'
		    
	titleStr += ']\n\n'
	
	return titleStr


def buildParametersList(params):
	parametersStr = ' \n\n+ Parameters\n'
	for param in params:
		parametersStr += '    + ' + param['name'] 
		
		if ('required' in param) : 
			parametersStr += ' (Required, ' if param['required'] else ' (Optional, '
		else:
			parametersStr += ' (Optional, '
		
		parametersStr += param['type'] + ') ... ' if 'type' in param else ') ... '
		parametersStr += param['description'] if 'description' in param else ''
		parametersStr += '\n'
	
	return parametersStr


def buildRequestBody(requestBody):
	requestBodyStr = ''
	if 'content' in requestBody:
		if 'application/json' in requestBody['content']:
			if 'schema' in requestBody['content']['application/json']:
				schema = requestBody['content']['application/json']['schema']
				example = generateExamples.buildObjectExample(schema)
		
				requestBodyStr += ' \n+ Request (application/json)\n```\n' 
				requestBodyStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True) 
				requestBodyStr += '\n```\n\n'
	return requestBodyStr


def buildExamples(responses):
	readMeStr = ''
	for code in sorted(responses.keys()):
		if 'content' in responses[code]:
			for type in sorted(responses[code]['content']):
				if 'example' in responses[code]['content'][type]:
					example = responses[code]['content'][type]['example']
				elif 'schema' in responses[code]['content'][type]:
					schema = responses[code]['content'][type]['schema']
					example = generateExamples.buildObjectExample(schema)
				else:
					example = {}
					
				readMeStr += '+ Response ' + code + ' (' + type + ')\n```\n'
				readMeStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True)
				readMeStr += '\n```\n\n'
	
	return readMeStr

def buildGroupTitle(callPath, callsStrings):
	groupTitles = callsStrings.keys()
	groupTitleStr = ''
	groupTitle = callPath.split('/')[1].lower()
	if groupTitle not in groupTitles:
		groupTitleStr += '\n\n## ' + groupTitle.capitalize() + ' [/brapi/v1/' + groupTitle + '] \n'
		callsStrings[groupTitle] = {'titleStr': groupTitleStr, 'depReadMeStrings': [], 'readMeStrings': []}
	
	return groupTitle
	
def buildReadMe(dir, fullBrAPI):
	readMeStr = ''
	with open(dir + 'GroupDescription.md', "r") as groupDescFile:
		readMeStr += groupDescFile.read() + '\n\n'
		
	callsStrings = {}
	for filename in sorted(glob.iglob(dir + '/**/*.yaml', recursive=True)):
		print(filename)
		fileObj = {}	
		with open(filename, "r") as stream:
			try:
				fileObj = yaml.load(stream)
				stream.close()
			except yaml.YAMLError as exc:
				print(exc)
		
		if 'paths' in fileObj:
			for callPath in fileObj['paths'].keys():
				groupTitle = buildGroupTitle(callPath, callsStrings)
				
				methods = fullBrAPI['paths'][callPath]
				methodKeys = sorted(fullBrAPI['paths'][callPath].keys())
				for methodKey in methodKeys:
					methodObj = methods[methodKey]
					
					desc = ''
					if 'description' in methodObj:
						desc = methodObj['description']
						
					deprecated = False
					if 'deprecated' in methodObj:
						deprecated = methodObj['deprecated']
					
					params = []
					if 'parameters' in methodObj:
						params = methodObj['parameters']
						
					responses = []
					if 'responses' in methodObj:
						responses = methodObj['responses']
						
					requestBody = {}
					if 'requestBody' in methodObj:
						requestBody = methodObj['requestBody']
					
					
					methodStr = '\n\n'
					methodStr += buildTitleStr(callPath, methodKey, params, deprecated)
					methodStr += desc
					methodStr += '\n\n'
					methodStr += buildParametersList(params)
					methodStr += '\n\n'
					methodStr += buildRequestBody(requestBody)
					methodStr += '\n\n'
					methodStr += buildExamples(responses)
					
					if deprecated:
						callsStrings[groupTitle]['depReadMeStrings'].append(methodStr)
					else:
						callsStrings[groupTitle]['readMeStrings'].append(methodStr)
				
	for title in callsStrings:
		readMeStr += callsStrings[title]['titleStr']
		for callDoc in callsStrings[title]['readMeStrings']:
			readMeStr += callDoc
		for depCallDoc in callsStrings[title]['depReadMeStrings']:
			readMeStr += depCallDoc
	
	return readMeStr
	

def go(rootPath, specificPath):
	fullBrAPI = derefernceAll.dereferenceBrAPI(filePath = rootPath + '/brapi_openapi.yaml')
	
	if specificPath == '' :
		for dir in glob.iglob(rootPath + '/Specification/**/', recursive=False):
			print(dir)
			readMeStr = buildReadMe(dir, fullBrAPI)
			with open(dir + '/README.md', 'w') as outfile:
				outfile.write(readMeStr)
	else:
		dir = rootPath + specificPath
		print(dir)
		readMeStr = buildReadMe(dir, fullBrAPI)
		# print(readMeStr)
		with open(dir + '/README.md', 'w') as outfile:
			outfile.write(readMeStr)
			

rootPath = '.'
specificPath = ''
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	specificPath = sys.argv[2];

#buildOpenAPI.go(rootPath)
go(rootPath, specificPath)
	
