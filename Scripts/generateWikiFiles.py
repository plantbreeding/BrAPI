#! /usr/bin/env python

import yaml
import glob
import sys
import json
import os
import requests
from time import sleep

def getObject(filename):
	fileObj = {}	
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			stream.close()
		except yaml.YAMLError as exc:
			print(exc)
	return fileObj

def getCallPages(fileObj):
	callPages = []
	
	if 'paths' in fileObj:
		for callPath in fileObj['paths']:
			for method in fileObj['paths'][callPath]:
				callObj = fileObj['paths'][callPath][method]
				callPage = {}
				callPage['name'] = method.upper() + '_' + callPath.replace('/', '_').replace('{', '').replace('}', '')
				
				contentStr = '{{note|This page is generated. All edits will be overridden automatically.}}'
				
				contentStr += '==Description==\n'
				contentStr += callObj['description'] + '\n'
				contentStr += '\n\n'
				
				if 'parameters' in callObj:
					contentStr += '==Parameters==\n'
					contentStr += '{| class="wikitable"\n'
					contentStr += '!Name\n'
					contentStr += '!Required\n'
					contentStr += '!Type\n'
					contentStr += '!Description\n'
					for param in callObj['parameters']:
						contentStr += '|-\n'
						contentStr += '|\'\'\'' + param['name'] + '\'\'\'\n'
						
						requiredStr = ''
						if 'required' in param:
							if param['required'] :
								requiredStr = '&#x2714;'
							else:
								requiredStr = ''
						else:
							requiredStr = ''
						contentStr += '|style="text-align:center;"|' + requiredStr + '\n'
						
						if 'type' in param :
							contentStr += '|' + param['type'].capitalize() + '\n'
						else: 
							contentStr += '|\n'
							
						if 'description' in param :
							contentStr += '|' + param['description'] + '\n'
						else: 
							contentStr += '|\n'
					contentStr += '|}\n'
						
				if 'responses' in callObj:
					for responseCode in callObj['responses']:
						contentStr += '==Response ' + responseCode + '==\n'
						responseObj = callObj['responses'][responseCode]
						if 'schema' in responseObj:
							contentStr += '===JSON Schema===\n'
							contentStr += ' ' + json.dumps(responseObj['schema'], indent=4, separators=(',', ': '), default=str, sort_keys=True).replace('\n', '\n ')
							contentStr += '\n'
						contentStr += '\n'
						
						if 'examples' in responseObj:
							contentStr += '===Examples===\n'
							for exampleType in responseObj['examples']:
								contentStr += '====' + exampleType + '====\n'
								exampleObj = responseObj['examples'][exampleType]
								if type(exampleObj) is dict:
									contentStr += ' ' + json.dumps(exampleObj, indent=4, separators=(',', ': '), default=str, sort_keys=True).replace('\n', '\n ')
								else:
									contentStr += ' ' + exampleObj
								contentStr += '\n'
						contentStr += '\n'
				
				contentStr += '\n\n'
				
				callPage['content'] = contentStr
				callPages.append(callPage)
	return callPages

def getObjectPages(openAPIObj):
	objectPages = []
	objectPage = {}
	objectPage['name'] = 'name'
	objectPage['content'] = 'content'
	objectPages.append(objectPage)
	return objectPages

def getCallsPage(openAPIObj):
	callsPage = {}
	callsPage['name'] = 'CallsPage'
	callsPage['content'] = 'content'
	return callsPage

def getObjectsPage(openAPIObj):
	objectsPage = {}
	objectsPage['name'] = 'ObjectsPage'
	objectsPage['content'] = 'content'
	return objectsPage
	
def login(username, password):	
	# get login token
	r1 = session.get(api_url, params={
	    'format': 'json',
	    'action': 'query',
	    'meta': 'tokens',
	    'type': 'login',
	})
	r1.raise_for_status()
	
	# log in
	r2 = session.post(api_url, data={
	    'format': 'json',
	    'action': 'login',
	    'lgname': username,
	    'lgpassword': password,
	    'lgtoken': r1.json()['query']['tokens']['logintoken'],
	})
	if r2.json()['login']['result'] != 'Success':
	    raise RuntimeError(r2.json()['login']['reason'])
	
	# get edit token
	r3 = session.get(api_url, params={
	    'format': 'json',
	    'action': 'query',
	    'meta': 'tokens',
	})
	return r3.json()['query']['tokens']['csrftoken']
	   
def pushPage(page, wikiToken, dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
	with open(dir + page['name'], 'w') as outfile:
		outfile.write(page['content'])
	
	r4 = session.post(api_url, data={
		'format': 'json',
		'action': 'edit',
		'assert': 'user',
		'text': page['content'],
		'summary': page['name'],
		'title': page['name'],
		'token': wikiToken,
	})
	
	print (r4.text)
	sleep(1)
	if 'error' in r4.json() :
		if r4.json()['error']['code'] == 'ratelimited':
			sleep(30)
			pushPage(page, wikiToken, dir)
		elif r4.json()['error']['code'] == 'badtoken':
			print(wikiToken)
   
def run(file, dir, wikiToken):
	openAPIObj = getObject(file)
	
	callPages = getCallPages(openAPIObj)
	for callPage in callPages:
		pushPage(callPage, wikiToken, dir + 'calls/')
		
	objectPages = getObjectPages(openAPIObj)
	for objectPage in objectPages:
		pushPage(objectPage, wikiToken, dir + 'objects/')
		
	callsPage = getCallsPage(openAPIObj)
	pushPage(callsPage, wikiToken, dir)
		
	objectsPage = getObjectsPage(openAPIObj)
	pushPage(objectsPage, wikiToken, dir)
		
api_url = 'https://wiki.brapi.org/api.php'
openAPIFile = './brapi_openapi.yaml'
outputDir = './wiki/'
userName = ''
passw = ''
if len(sys.argv) > 1 :
	openAPIFile = sys.argv[1];
if len(sys.argv) > 2 :
	userName = sys.argv[2];
if len(sys.argv) > 3 :
	passw = sys.argv[3];

session = requests.Session()
wikiToken = login(userName, passw)
run(openAPIFile, outputDir, wikiToken)
