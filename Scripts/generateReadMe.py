#! /usr/bin/env python

import yaml
import glob
import sys
import json


def buildReadMe(dir):
	readMeStr = ''
	with open(dir + 'GroupDescription.md', "r") as groupDescFile:
		readMeStr += groupDescFile.read() + '\n\n'
		
	for filename in sorted(glob.iglob(dir + '/*.yaml', recursive=True)):
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
			methodKeys = sorted(fileObj['paths'][callPath].keys())
			for methodKey in methodKeys:
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
						body = param['schema']['$ref'][1:] if '$ref' in param['schema'] else json.dumps(param['schema'], indent=4, separators=(',', ': '), default=str)
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
						readMeStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True)
						readMeStr += '\n```'
	return readMeStr
	

rootPath = '.'
specificPath = ''
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	specificPath = sys.argv[2];

if specificPath == '' :
	for dir in glob.iglob(rootPath + '/**/', recursive=False):
		print(dir)
		readMeStr = buildReadMe(dir)
		with open(dir + '/README.md', 'w') as outfile:
			outfile.write(readMeStr)
else:
	dir = rootPath + specificPath
	print(dir)
	readMeStr = buildReadMe(dir)
	print(readMeStr)
	with open(dir + '/README.md', 'w') as outfile:
		outfile.write(readMeStr)
	
		

	
