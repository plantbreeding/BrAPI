#! /usr/bin/env python

import yaml
import glob
import sys
import json
import requests
from copy import deepcopy
import jsonschema
from jsonschema import validate

def getObjectExample(schema, path, method):
	url = 'http://localhost:8080/brapi/v1' + replaceIDs(path)
	headers = {'Authorization':'Bearer YYYY'}
	if method == 'get':
		params = getParams(path)
		res = requests.get(url, params, headers=headers)
	elif method == 'post' :
		params = postParams(path)
		res = requests.post(url, json=params, headers=headers)
	elif method == 'put' :
		params = putParams(path)
		res = requests.put(url, json=params, headers=headers)
		
	try :
		example = res.json()
	except:
		print('Bad JSON')
		print(method + ' ' + url)
		print(res)
		return None
	
	if not res.ok :
		print('Bad Response Code')
		print(method + ' ' + url)
		print(example)
		return None
		
	try :
		if res.ok :
			validate(example, schema)
	except jsonschema.exceptions.ValidationError as ve:
		print('Bad Schema Match')
		print(method + ' ' + url)
		print(str(ve) + "\n")
		return example
	
	return example

def addExamples(obj):
	if('paths' in obj):
		for path in obj['paths']:
			for method in obj['paths'][path]:
				for responseCode in obj['paths'][path][method]['responses']:
					if 'content' in obj['paths'][path][method]['responses'][responseCode]:
						response = obj['paths'][path][method]['responses'][responseCode]['content']['application/json']
						if ('schema' in response):
							schema = dereferenceAll(deepcopy(response['schema']))
							newExample = getObjectExample(schema, path, method)
							if newExample is not None :
								print('.')
								obj['paths'][path][method]['responses'][responseCode]['content']['application/json']['example'] = newExample
								if 'examples' in obj['paths'][path][method]['responses'][responseCode]['content']['application/json']:
									obj['paths'][path][method]['responses'][responseCode]['content']['application/json'].pop('examples')
						
	return obj

def dereferenceAll(obj, modelsPath = 'C:/Users/ps664/Documents/BrAPI/API/Specification/ModelDefinitions/'):
	if type(obj) is dict:
		for fieldStr in obj:
			if(fieldStr == '$ref'):
				refName = obj[fieldStr].split('/')[3]
				path = modelsPath + refName + '.yaml'
				refObj = dereferenceAll(readFileToDict(path)['components']['schemas'][refName])
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

def replaceIDs(url):
	newURL = url
	newURL = newURL.replace('{studyDbId}', '1001')
	newURL = newURL.replace('{mapDbId}', 'gm1')
	newURL = newURL.replace('{breedingMethodDbId}', 'bm1')
	newURL = newURL.replace('{germplasmDbId}', '3')
	newURL = newURL.replace('{locationDbId}', '1')
	newURL = newURL.replace('{observationVariableDbId}', 'MO_123:100002')
	newURL = newURL.replace('{traitDbId}', '1')
	newURL = newURL.replace('{trialDbId}', '101')
	newURL = newURL.replace('{markerDbId}', 'mr2')
	newURL = newURL.replace('{markerprofileDbId}', 'mp1')
	newURL = newURL.replace('{linkageGroupName}', '1')
	newURL = newURL.replace('{sampleDbId}', 'sam1')
	newURL = newURL.replace('{vendorPlateDbId}', 'pl1')
	return newURL

def postParams(path):
	params = {'pageSize': 2}
	if path == '/vendor/plates':
		params = {
		  "plates": [
		    {
		      "clientPlateDbId": "string",
		      "plateFormat": "string",
		      "sampleType": "string",
		      "samples": [
		        {
		          "column": "1",
		          "concentration": "string",
		          "row": "0",
		          "sampleDbId": "string",
		          "taxonId": {
		            "sourceName": "string",
		            "taxonId": "string"
		          },
		          "tissueType": "string",
		          "volume": "string",
		          "well": "1"
		        }
		      ],
		      "vendorProjectDbId": "string"
		    }
		  ]
		}
	elif path == '/phenotypes':
		params = {
		  "data": [
		    {
		      "observatioUnitDbId": "1",
		      "observations": [
		        {
		          "collector": "string",
		          "observationDbId": "string",
		          "observationTimeStamp": "2018-09-19T15:57:27.903Z",
		          "observationVariableDbId": "MO_123:100002",
		          "observationVariableName": "string",
		          "season": "fall 2011",
		          "value": "string"
		        }
		      ],
		      "studyDbId": "string"
		    }
		  ]
		}
	elif path == '/markers-search' : 
		params['includeSynonyms'] = 'true'
	return params

def putParams(path):
	params = {'pageSize': 2}
	if path == '/samples':
		params = {
		  "germplasmDbId": "1",
		  "notes": "string",
		  "observationUnitDbId": "1",
		  "plantDbId": None,
		  "plateDbId": "string",
		  "plateIndex": 0,
		  "plotDbId": "1",
		  "sampleDbId": "string",
		  "sampleTimestamp": "2018-09-25T21:07:17.505Z",
		  "sampleType": "string",
		  "studyDbId": "1001",
		  "takenBy": "string",
		  "tissueType": "string"
		}
	elif path == '/studies/{studyDbId}/layout':
		params = {
		  "layout": [
		    {
		      "X": 10,
		      "Y": 12,
		      "blockNumber": 0,
		      "entryType": "CHECK",
		      "observationUnitDbId": "1",
		      "replicate": 0
		    }
		  ]
		}
	elif path == '/studies/{studyDbId}/observationunits':
		params = [{}]
	return params

def getParams(path):
	params = {'pageSize': 2}
	if path == '/markers-search' : 
		params['includeSynonyms'] = 'true'
	elif path == '/markers':
		params['include'] = 'synonyms'
	elif path == '/germplasm/{germplasmDbId}/pedigree':
		params['includeSiblings'] = 'true'
	return params

rootPath = './'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

if(rootPath[-1] == '/'):
	rootPath = rootPath + '**/*.yaml'

for filename in glob.iglob(rootPath, recursive=True):
	#print(filename)
	file = readFileToDict(filename)	
	newFile = addExamples(file)
	
	with open(filename, 'w') as outfile:
		yaml.dump(newFile, outfile, default_flow_style=False, width=float("inf"))
	
		

	
