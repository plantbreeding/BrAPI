#! /usr/bin/env python

import yaml
import glob
import sys
import json
import dereferenceAll
import re

def buildStringExample(fieldName, strSchema):
	strExample = ''
	if('enum' in strSchema):
		strExample = strSchema['enum']
	elif('format' in strSchema):
		if 'date' == strSchema['format']:
			strExample = '2018-01-01'
		elif 'date-time' == strSchema['format']:
			strExample = '2018-01-01T14:47:23-0600'
	else:
		strExample = fieldName
		print('WARNING: generic String example generated, example missing from spec in ' + fieldName)
		
	return strExample

def buildArrayExample(fieldName, schema):
	arr = []
	
	if 'example' in schema:
		arr = schema['example']
	elif 'items' in schema:
		itemSchema = schema['items']
		if ('type' in itemSchema):
			if (itemSchema['type'] == 'string'):
				print('WARNING: generic String List example generated, example missing from spec in ' + fieldName)
				arr = [fieldName + '1', fieldName + '2']
			elif (itemSchema['type'] == 'int'):
				print('WARNING: generic Int List example generated, example missing from spec in ' + fieldName)
				arr = [1, 2]
			elif (itemSchema['type'] == 'array'):
				arr.append(buildArrayExample(fieldName, itemSchema))
			elif (itemSchema['type'] == 'object'):
				arr.append(buildObjectExample(itemSchema))
		elif ('properties' in itemSchema):
			arr.append(buildObjectExample(itemSchema))
		
	return arr

def buildObjectExample(schema):
	example = {}
	
	if ('example' in schema):
		example = schema['example']
	elif ('properties' in schema):
		for fieldName in schema['properties']:
			fieldObj = schema['properties'][fieldName]
			
			if ('example' in fieldObj):
				example[fieldName] = fieldObj['example']
			elif ('type' in fieldObj):
				if (fieldObj['type'] == 'string'):
					example[fieldName] = buildStringExample(fieldName, fieldObj)
				elif (fieldObj['type'] == 'integer'):
					example[fieldName] = 0
					print('WARNING: generic Int example generated, example missing from spec in ' + fieldName)
				elif (fieldObj['type'] == 'array'):
					example[fieldName] = buildArrayExample(fieldName, fieldObj)
				elif (fieldObj['type'] == 'object'):
					example[fieldName] = buildObjectExample(fieldObj)
			elif ('properties' in fieldObj):
				example[fieldName] = buildObjectExample(fieldObj)
			
	return example

def buildGroupTitle(callPath, method, callsStrings):
	groupTitles = callsStrings.keys()
	groupTitle = method + '_' + callPath
	if groupTitle not in groupTitles:
		groupTitleStr = '\n## '
		groupTitleStr += method.capitalize() + ' - ' + re.sub('{.*}', '{ID}', callPath)
		groupTitleStr += ' [/brapi/v1/' + callPath + '] \n'
		
		callsStrings[groupTitle] = {'titleStr': groupTitleStr, 'depReadMeStrings': [], 'readMeStrings': []}
	
	return groupTitle

def buildTitleStr(path, method = 'GET', params = [], deprecated = False):

	titleStr = '\n### ' 
	if deprecated:
		titleStr += '**Deprecated** '
		
	titleStr += path
	
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
		parametersStr += re.sub(r'\n', '', param['description']) if 'description' in param else ''
		parametersStr += '\n'
	
	return parametersStr


def buildRequestBody(requestBody):
	requestBodyStr = ''
	if 'content' in requestBody:
		if 'application/json' in requestBody['content']:
			if 'schema' in requestBody['content']['application/json']:
				schema = requestBody['content']['application/json']['schema']
				example = ''
				
				if 'type' in schema:
					if 'object' == schema['type']:
						example = buildObjectExample(schema)
					elif 'array' == schema['type']:
						example = buildArrayExample('request', schema)
		
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
					example = buildObjectExample(schema)
				else:
					example = {}
					
				readMeStr += '+ Response ' + code + ' (' + type + ')\n```\n'
				readMeStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True)
				readMeStr += '\n```\n\n'
	
	return readMeStr

def buildRequestDefTable(obj):
	table = ''
	if 'content' in obj:
		if 'application/json' in obj['content']:
			if 'schema' in obj['content']['application/json']:
				table = '**Request Fields** \n\n|Field|Type|Description|\n|---|---|---| \n'
				schema = obj['content']['application/json']['schema']
				table += buildObjectTableRow(schema)
	return table

def buildResponseDefTable(responses):
	table = ''
	if '200' in responses:
		if 'content' in responses['200']:
			if 'application/json' in responses['200']['content']:
				if 'schema' in responses['200']['content']['application/json']:
					if 'properties' in responses['200']['content']['application/json']['schema']:
						if 'result' in responses['200']['content']['application/json']['schema']['properties']:
							table = '**Response Fields** \n\n|Field|Type|Description|\n|---|---|---| \n'
							schema = responses['200']['content']['application/json']['schema']['properties']['result']
							table += buildObjectTableRow(schema)
	return table

def buildObjectTableRow(schema, parentPrefix = ''):
	row = ''
	if 'properties' in schema:
		for prop in sorted(schema['properties'].keys()):
			#print(prop)
			#print(schema['properties'][prop].keys())
			
			field = prop
			type = ''
			desc = ''
			
			if 'type' in schema['properties'][prop]:
				type = schema['properties'][prop]['type']
				if 'format' in schema['properties'][prop]:
					type += ' (' + schema['properties'][prop]['format'] + ')'
			if type == 'array' and 'type' in schema['properties'][prop]['items']:
				type += '[' +  schema['properties'][prop]['items']['type'] + ']'
			if 'description' in schema['properties'][prop]:
				desc = schema['properties'][prop]['description'].replace('\n', ' ').replace('|', '')
			
			
			row += '|' +  field + '|' + type + '|' + desc + '|\n'
			
			
			if type == 'object' and 'properties' in schema['properties'][prop]:
				row += buildObjectTableRow(schema['properties'][prop])
			elif type[:5] == 'array' and 'properties' in schema['properties'][prop]['items']:
				row += buildObjectTableRow(schema['properties'][prop]['items'])
	elif 'items' in schema:
		row += buildObjectTableRow(schema['items'])
			
	return row

def buildReadMe(dir, fullBrAPI):
	readMeStr = ''
	with open(dir + 'GroupDescription.md', "r") as groupDescFile:
		readMeStr += groupDescFile.read() + '\n\n'
		
	callsStrings = {}
	for filename in sorted(glob.iglob(dir + '/**/*.yaml', recursive=True)):
		fileObj = {}	
		with open(filename, "r") as stream:
			try:
				fileObj = yaml.load(stream)
				stream.close()
			except yaml.YAMLError as exc:
				print(exc)
		
		if 'paths' in fileObj:
			for callPath in sorted(fileObj['paths'].keys()):				
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
					methodStr += buildRequestDefTable(requestBody)
					methodStr += '\n\n'
					methodStr += buildResponseDefTable(responses)
					methodStr += '\n\n'
					methodStr += buildParametersList(params)
					methodStr += '\n\n'
					methodStr += buildRequestBody(requestBody)
					methodStr += '\n\n'
					methodStr += buildExamples(responses)
					
					groupTitle = buildGroupTitle(callPath, methodKey, callsStrings)
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
	

def buildReadMes(rootPath, specificPath):
	fullBrAPI = dereferenceAll.dereferenceBrAPI(filePath = rootPath + '/brapi_openapi.yaml')
	
	for dir in glob.iglob(rootPath + specificPath + '/', recursive=False):
		print("dir - " + dir)
		readMeStr = buildReadMe(dir, fullBrAPI)
		fileName = dir + '/README.md'
		with open(fileName, 'w') as outfile:
			outfile.write(readMeStr)
			print("fileName - " + fileName)
			
def buildGitHubReadMe(rootPath):
	sources=[  "GeneralInfo/Intro.md",
		       "GeneralInfo/URL_Structure.md",
		       "GeneralInfo/Response_Structure.md",
		       "GeneralInfo/Error_Handling.md",
		       "GeneralInfo/Date_Time_Encoding.md",
		       "GeneralInfo/Location_Encoding.md",
		       "GeneralInfo/Search_Services.md",
		       "GeneralInfo/Asychronous_Processing.md"
	       ]
		
	outFilePath = rootPath + '/Specification/README.md'
	with open(outFilePath, "w") as outFile:
		for source in sources:
			filename = rootPath + '/Specification/' + source
			with open(filename, "r") as inFile:
				outFile.write(inFile.read())
	
		print("outFilePath - " + outFilePath)


rootPath = '.'
specificPath = '**'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	specificPath = sys.argv[2];

#buildOpenAPI.go(rootPath)
buildReadMes(rootPath, specificPath)
#buildGitHubReadMe(rootPath)
	
