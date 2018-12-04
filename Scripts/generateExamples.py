#! /usr/bin/env python

import yaml
import glob
import sys
import json
import requests
from copy import deepcopy
import jsonschema
from jsonschema import validate
import dereferenceAll
import testInputs


def getObjectExample(schema, path, method):
	url = 'http://localhost:8080/brapi/v1' + testInputs.replaceIDs(path)
	headers = {'Authorization':'Bearer YYYY'}
	if method == 'get':
		params = testInputs.getParams(path)
		res = requests.get(url, params, headers=headers)
	elif method == 'post' :
		params = testInputs.postParams(path)
		res = requests.post(url, json=params, headers=headers)
	elif method == 'put' :
		params = testInputs.putParams(path)
		res = requests.put(url, json=params, headers=headers)
		
	try :
		example = res.json()
	except:
		if verbose:
			print('Bad JSON')
			print(method + ' ' + url)
			print(res)
		else:
			print('X1 - ' + method + ' ' + url)
		return None
	
	if not res.ok :
		if verbose:
			print('Bad Response Code')
			print(method + ' ' + url)
			print(example)
		else:
			print('X2 - ' + method + ' ' + url)
		return None
		
	try :
		if res.ok :
			validate(example, schema)
	except jsonschema.exceptions.ValidationError as ve:
		if verbose:
			print('Bad Schema Match')
			print(method + ' ' + url)
			print(str(ve) + "\n")
		else:
			print('X3 - ' + method + ' ' + url)
		return example
	
	return example


def addExamples(obj, parent):	
	if('paths' in obj):
		for path in obj['paths']:
			for method in obj['paths'][path]:
				for responseCode in obj['paths'][path][method]['responses']:
					if 'content' in obj['paths'][path][method]['responses'][responseCode]:
						response = obj['paths'][path][method]['responses'][responseCode]['content']['application/json']
						if ('schema' in response):
							schema = dereferenceAll.dereferenceAll(deepcopy(response['schema']), parent)
							newExample = getObjectExample(schema, path, method)
							if newExample is not None :
								# print('.')
								obj['paths'][path][method]['responses'][responseCode]['content']['application/json']['example'] = newExample
								if 'examples' in obj['paths'][path][method]['responses'][responseCode]['content']['application/json']:
									obj['paths'][path][method]['responses'][responseCode]['content']['application/json'].pop('examples')
						
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



rootPath = './Specification/'
verbose = False

if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	verbose = sys.argv[2] == '-v';

if(rootPath[-1] == '/'):
	rootPath = rootPath + '**/*.yaml'
	
parentFile = dereferenceAll.dereferenceBrAPI()

for filename in glob.iglob(rootPath, recursive=True):
	# print(filename)
	file = readFileToDict(filename)	
	newFile = addExamples(file, parentFile)
	
	with open(filename, 'w') as outfile:
		yaml.dump(newFile, outfile, default_flow_style=False, width=float("inf"))
		
	
