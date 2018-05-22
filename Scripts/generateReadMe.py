#! /usr/bin/env python

import yaml
import glob
import sys
import json

rootPath = '.'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

readMeStr = ''
for filename in glob.iglob(rootPath + '/**/*.yaml', recursive=True):
	print(filename)
	fileObj = {}	
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			print(exc)
	
	if 'paths' in fileObj:
		callPath = list(fileObj['paths'].keys())[0]
		methods = fileObj['paths'][callPath]
		for methodKey in methods.keys():
			methodObj = methods[methodKey]
			
			desc = ''
			if 'description' in methodObj:
				desc = methodObj['description']
			
			params = []
			if 'parameters' in methodObj:
				params = methodObj['parameters']
				
			responses = []
			if 'responses' in methodObj:
				responses = methodObj['responses']
			
			readMeStr += '\n\n## ' + callPath[1:].capitalize() + ' [' + methodKey.capitalize() + ' /brapi/v1' + callPath
			for param in params:
				if param['in'] == 'query' :
				    readMeStr += '{?' + param['name'] + '}'
				    
			readMeStr += ']\n\n' + desc
			readMeStr += ' \n\n+ Parameters\n'
			body = ''
			for param in params:
				if param['in'] == 'body':
					body = param['schema']['$ref'][1:]
				else:
					readMeStr += '    + ' + param['name'] 
					
					if ('required' in param) : 
						readMeStr += ' (Required, ' if param['required'] else ' (Optional, '
					else:
						readMeStr += ' (Optional, '
					
					readMeStr += param['type'] + ') ... ' if 'type' in param else ') ... '
					readMeStr += param['description'] if 'description' in param else ''
					readMeStr += '\n'
			
			if body != '' :
				readMeStr += ' \n+ Request (application/json)\n' + body
				
			
			readMeStr += '\n\n'
			for code in responses:
				for type in responses[code]['examples']:
					example = responses[code]['examples'][type]
					readMeStr += '+ Response ' + code + ' (' + type + ')\n```\n'
					readMeStr += json.dumps(example, indent=4, separators=(',', ': '))
					readMeStr += '\n```'

	

print(readMeStr)
	
with open(rootPath + '/README.md.gen', 'w') as outfile:
	outfile.write(readMeStr)
