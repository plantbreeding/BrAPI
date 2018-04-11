#! /usr/bin/env python

import yaml
import glob
import sys
from pip._vendor.distlib.compat import raw_input

rootPath = '.'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

descriptionDict = {}

for filename in glob.iglob(rootPath + '/**/*.yaml', recursive=True):
	print('')
	print('---- ' + filename + ' ----')
	fileObj = {}
	fileChanged = False
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			print(exc)
	
	
	if 'paths' in fileObj:
		methods = fileObj['paths'][list(fileObj['paths'].keys())[0]]
		for method in methods.keys():
			print(filename + ' -> ' + method + ' -> description')
			
			desc = ''
			if 'description' in methods[method]:
				desc = methods[method]['description']
			userInput = raw_input('  > ' + desc)
				
			if userInput == 'X':
				raise Exception
			elif userInput != '':
				fileChanged = True
				methods[method]['description'] = userInput
			
			print('')
			
			if 'parameters' in methods[method]:
				for parameter in methods[method]['parameters']:
					print(filename + ' -> ' + method + ' -> param:' + parameter['name'])
	
					paramDesc = ''
					if 'description' in parameter:
						paramDesc = parameter['description']
					paramUserInput = raw_input('  > ' + paramDesc)
						
					if paramUserInput == 'X':
						raise Exception
					elif paramUserInput != '':
						fileChanged = True
						methods[method]['description'] = paramUserInput
	
#	if 'definitions' in fileObj:
#		props = fileObj['definitions'][list(fileObj['definitions'].keys())[0]]['properties']
#		for prop in props.keys():
#			print(filename + '->' + prop)
#			
#			if 'description' in props[prop]:
#				##print('  Description: ' + props[prop]['description'])
#				descriptionDict[prop] = props[prop]['description']
#				
#			else:
#				fileChanged = True
#				
#				if prop in descriptionDict:
#					desc = raw_input('  > ' + descriptionDict[prop]) 
#					if desc == '':
#						desc = descriptionDict[prop]
#				else:
#					desc = raw_input('  > ') 
#					
#				if desc == 'X':
#					raise Exception
#				
#				props[prop]['description']  = desc
#				descriptionDict[prop] = desc
#				
#				print('  ' + props[prop]['description'])
#				print('')
		
		
		if fileChanged:
			with open(filename, 'w') as outfile:
				yaml.dump(fileObj, outfile, default_flow_style=False, width=float("inf"))
