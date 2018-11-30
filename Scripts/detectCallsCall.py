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
import brapiVersions

##----------------------------------------------------------------------

class callObj:
	
	def __init__(self, call):
		self.call = call
		self.methods = []
		self.datatypes = ["application/json"]
		self.dataTypes = ["application/json"]
		self.versions = []
	
	def __repr__(self):
		return self.__str__()
	
	def __str__(self):
		## Not used
		##callSpacerTabs = 4 - (len(self.call) // 4)
		##return "{\"call\": \"" + self.call +"\", " + ("\t" * callSpacerTabs) + "\"methods\": " + str(self.methods) + ",\t\"dataTypes\": " + str(self.dataTypes) +",\t\"datatypes\": " + str(self.datatypes) +",\t\"versions\": " + str(self.versions) +"}\n"
		return self.call
	
	def addMethod(self, method):
		self.methods.append(method)
	
	def addDataType(self, dataType):
		self.dataTypes.append(dataType)
		
	def addVersions(self, version):
		self.versions = list(set(self.versions + version))
		self.versions.sort()
		
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
			
			call.addVersions(brapiVersions.getVersions(path, method))
		
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

rawOut = ""
for callraw in calls:
	rawOut += json.dumps(callraw, cls=MyEncoder) + "\n"

r = requests.get(baseURL + '/calls', {'page' : 0, 'pageSize' : 200})
actual = json.dumps(r.json(), indent=4, separators=(',', ': '), sort_keys=True, cls=MyEncoder)

with open('./out/CallsCall_expected.json', 'w') as outfile:
	outfile.write(expected)
with open('./out/CallsCall_expected_raw.json', 'w') as outfile:
	outfile.write(rawOut)
with open('./out/CallsCall_actual.json', 'w') as outfile:
	outfile.write(actual)

print(unavCalls)
print(badCalls)


