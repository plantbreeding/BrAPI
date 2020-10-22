#! /usr/bin/env python

import yaml
import glob
import sys
import json
import os
import requests
from time import sleep

def login(session, username, password):	
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

def downloadAllPages(session, dir):
	allPagesResponse = session.get(api_url, params={
	    'format': 'json',
	    'action': 'query',
	    'list': 'allpages',
	    'aplimit': 'max',
	})
	
	allpages = allPagesResponse.json()['query']['allpages']
	
	for page in allpages:
		
		pageContentResponse = session.get(api_url, params={
		    'format': 'json',
		    'action': 'parse',
		    'prop': 'wikitext',
		    'formatversion': '2',
		    'pageid': page['pageid']
		})
		
		outFilePath = dir + page['title'].replace('/', '-') + '.wiki'
		fullText = pageContentResponse.json()['parse']['wikitext']
		
		with open(outFilePath, "w") as outFile:
			outFile.write(fullText)
			print(outFilePath)

def restoreAllPages(session, outputDir, wikiToken):
	filenames = glob.glob(outputDir + '/**/*.wiki', recursive=True)
	for file in filenames:
		pageTitle = os.path.basename(file)[:-5]
		print(pageTitle)
		pageContent = ''
		with open(file, "r") as inFile:
			pageContent += inFile.read()
			
		pushPage(session, pageTitle, pageContent, wikiToken)


def pushPage(session, pageTitle, pageContent, wikiToken):
		
	r4 = session.post(api_url, data={
		'format': 'json',
		'action': 'edit',
		'assert': 'user',
		'text': pageContent,
		'summary': pageTitle,
		'title': pageTitle,
		'token': wikiToken,
	})
	
	print (r4.text)
	sleep(1)
	if 'error' in r4.json() :
		if r4.json()['error']['code'] == 'ratelimited':
			print('too many uploads, sleeping for 30 sec')
			sleep(30)
			pushPage(session, pageTitle, pageContent, wikiToken)
		elif r4.json()['error']['code'] == 'badtoken':
			print(wikiToken)

   
def main():
	outputDir = '../Wiki/'
	userName = ''
	passw = ''
	
	if '-out' in sys.argv:
		i = sys.argv.index('-out')
		outputDir = sys.argv[i + 1]
		if outputDir[-1] != '/':
			outputDir = outputDir + '/'
			
	if '-un' in sys.argv:
		i = sys.argv.index('-un')
		userName = sys.argv[i + 1]

	if '-pw' in sys.argv:
		i = sys.argv.index('-pw')
		passw = sys.argv[i + 1]
	
	
	session = requests.Session()
	if '-restore' in sys.argv:
		wikiToken = login(session, userName, passw)
		restoreAllPages(session, outputDir, wikiToken)
	else:
		downloadAllPages(session, outputDir)

api_url = 'https://wiki.brapi.org/api.php'
main()
