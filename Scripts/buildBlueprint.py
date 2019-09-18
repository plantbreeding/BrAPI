#! /usr/bin/env python

import sys
import json
import glob
import yaml
import re

def go():
		
	rootPath = '.'
	if len(sys.argv) > 1 :
	    rootPath = sys.argv[1]
	if rootPath[-1] != '/':
		rootPath = rootPath + '/'
	
	headerHTML = ''
	with open(rootPath + "swaggerMetaData.yaml", "r") as headerFile:
		try:
			fileObj = yaml.load(headerFile)
			if 'info' in fileObj:
				if 'description' in fileObj['info']:
					headerHTML = parseHTMLToMD(fileObj['info']['description'])
					
		except yaml.YAMLError as exc:
			print(exc)
	
	sources = sorted(glob.glob(rootPath + '**/README.md', recursive=True))

	fullText = headerHTML
	for source in sources:
		with open(source, "r") as inFile:
			fullText += inFile.read()
	
	outFilePath = rootPath + '/brapi_blueprint.apib'
	with open(outFilePath, "w") as outFile:
		outFile.write(fullText)
		print(outFilePath)
		
	outREADMEFilePath = rootPath + '/README.md'
	with open(outREADMEFilePath, "w") as outRMFile:
		outRMFile.write(fullText)
		print(outREADMEFilePath)
		
	outFileJsonPath = rootPath + '/brapi_blueprint.apib.json'
	with open(outFileJsonPath, "w") as outFileJson:
		jsonWrapper = {'code': fullText}
		json.dump(jsonWrapper, outFileJson)
		print(outFileJsonPath)
			
def parseHTMLToMD(htmlStr):
	title = re.search(r'<div class="[^"]*current-brapi-section[^"]*">\n\s*<h2 class="brapi-section-title">([^<]*)</h2>', htmlStr).group(1)
		
	body = re.sub(r'<h2 class="brapi-section-title">([^<]*)</h2>', r'### \1', htmlStr)
	body = re.sub(r'<div class="brapi-section-description">([^<]*)</div>', r'\1', body)
	body = re.sub(r'<div class="version-number">([^<]*)</div>\n', r'\n\1', body)
	body = re.sub(r'<div class="stop-float"></div>', r'', body)
	body = re.sub(r'<div class="[^"]*brapi-section[^"]*">', r'', body)
	body = re.sub(r'\n\s*</div>', r'\n', body)
	body = re.sub(r'<div class="link-btn"><a.*href="([^"]*)">([^<]*)</a></div>\n', r' - [\2](\1)', body)
	body = re.sub(r'<div class="gen-info-link"><a.*href="([^"]*)">([^<]*)</a></div>', r'- [\2](\1)', body)
	body = re.sub(r'<style>[^<]*</style>', r'\n', body)
	
	body = re.sub(title, '**' + title + '**', body)
	
	mdStr = 'FORMAT: 1A\n\n# ' + title + '\n\n' + body
	
	return mdStr
			
go()