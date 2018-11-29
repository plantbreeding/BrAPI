#! /usr/bin/env python

import yaml
import sys
import requests
import re
import json
from json import JSONEncoder
from pip._vendor.distlib.compat import raw_input
import dereferenceAll
import testInputs

##----------------------------------------------------------------------

class callObj:
	
	def __init__(self, call):
		self.call = call
		self.methods = []
		self.datatypes = ["application/json"]
		self.versions = ["1.0", "1.1", "1.2", "1.3"]
	
	def __repr__(self):
		return self.__str__()
	
	def __str__(self):
		return "\
{\n\
\tcall: \"" + self._call +"\",\n\
\tmethods: " + str(self._methods) + ",\n\
\tdataTypes: " + str(self._dataTypes) +",\n\
\tdatatypes: " + str(self._dataTypes) +",\n\
\tversions: " + str(self._versions) +"\n\
}"
	
	def addMethod(self, method):
		self.methods.append(method)
	
	def addDataType(self, dataType):
		self.dataTypes.append(dataType)
		
	def addVersion(self, version):
		self.versions.append(version)
		
##----------------------------------------------------------------------

class MyEncoder(JSONEncoder):
	def default(self, o):
	    return o.__dict__    

##----------------------------------------------------------------------

fileObj = dereferenceAll.dereferenceBrAPI('./brapi_openapi.yaml')

baseURL = 'http://localhost:8080/brapi/v1'
change = raw_input('Test URL (default: ' + baseURL + ') > ')
if change != '':
	baseURL = change

calls = []
unavCalls = []
badCalls = []

reg = re.compile('\{[^\{\}]*\}')

if 'paths' in fileObj:
	for path in list(fileObj['paths'].keys()):
		testURL = ''
		if(baseURL[-1:] == '/'):
			testURL = baseURL[:-1] + testInputs.replaceIDs(path)
		else:
			testURL = baseURL + testInputs.replaceIDs(path)
			
		call = callObj(path[1:])
		for method in list(fileObj['paths'][path].keys()):
			r = {}
			if method == 'get':
				r = requests.get(testURL)
			elif method == 'post':
				r = requests.post(testURL, json={})
			elif method == 'put':
				r = requests.put(testURL, json={})
			elif method == 'delete':
				r = requests.delete(testURL)
		
			if(r.status_code == 200):
				call.addMethod(method.upper())
			elif(r.status_code == 404):
				unavCalls.append(method + ' ' + path)
			else:
				badCalls.append(str(r.status_code) + ' ' + method + ' ' + path)
				call.addMethod(method.upper())
		
		if call.methods:
			calls.append(call)

expectedJson = {
	"metadata" : {
		"pagination": {
            "totalCount": len(calls),
            "currentPage": 0,
            "totalPages": 1,
            "pageSize": len(calls)
        },
        "status": [],
        "datafiles": []
        },
	"result": {
		"data": calls
		}
	}
expected = json.dumps(expectedJson, indent=4, separators=(',', ': '), sort_keys=True,  cls=MyEncoder)

r = requests.get(baseURL + '/calls', {'page' : 0, 'pageSize' : 100})
actual = json.dumps(r.json(), indent=4, separators=(',', ': '), sort_keys=True, cls=MyEncoder)

with open('./out/CallsCall_expected.json', 'w') as outfile:
	outfile.write(expected)
with open('./out/CallsCall_actual.json', 'w') as outfile:
	outfile.write(actual)

print(unavCalls)
print(badCalls)


