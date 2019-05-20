#! /usr/bin/env python

import yaml
import glob
import sys
import json
import dereferenceAll

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
				example = buildObjectExample(schema)
		
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

def buildGroupTitle(callPath, callsStrings):
	groupTitles = callsStrings.keys()
	groupTitleStr = ''
	groupTitle = callPath.split('/')[1].lower()
	if groupTitle not in groupTitles:
		groupTitleStr += '\n\n## ' + groupTitle.capitalize() + ' [/brapi/v1/' + groupTitle + '] \n'
		callsStrings[groupTitle] = {'titleStr': groupTitleStr, 'depReadMeStrings': [], 'readMeStrings': []}
	
	return groupTitle

def buildRequestDefTable(obj):
	table = ''
	if 'content' in obj:
		if 'application/json' in obj['content']:
			if 'schema' in obj['content']['application/json']:
				table = '**Request Fields** \n |Field|Type|Description|\n|---|---|---| \n'
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
							table = '**Response Fields** \n |Field|Type|Description|\n|---|---|---| \n'
							schema = responses['200']['content']['application/json']['schema']['properties']['result']
							table += buildObjectTableRow(schema)
	return table

def buildObjectTableRow(schema, parentPrefix = ''):
	row = ''
	if 'properties' in schema:
		for prop in schema['properties']:
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
		#print(filename)
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
					methodStr += buildRequestDefTable(requestBody)
					methodStr += '\n\n'
					methodStr += buildResponseDefTable(responses)
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
	

def buildReadMes(rootPath, specificPath):
	fullBrAPI = dereferenceAll.dereferenceBrAPI(filePath = rootPath + '/brapi_openapi.yaml')
	
	for dir in glob.iglob(rootPath + '/Specification/' + specificPath + '/', recursive=False):
		readMeStr = buildReadMe(dir, fullBrAPI)
		fileName = dir + '/README.md'
		with open(fileName, 'w') as outfile:
			outfile.write(readMeStr)
			print(fileName)
			
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
	
		print(outFilePath)


rootPath = '.'
specificPath = '**'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	specificPath = sys.argv[2];

#buildOpenAPI.go(rootPath)
buildReadMes(rootPath, specificPath)
buildGitHubReadMe(rootPath)
	
