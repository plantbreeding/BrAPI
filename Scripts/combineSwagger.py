#! /usr/bin/env python

import yaml
import glob
import sys

rootPath = '.'
metaFilePath = './swaggerMetaData.yaml'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	metaFilePath = sys.argv[2];

paths = {}
defin = {}

for filename in glob.iglob(rootPath + '/**/*.yaml', recursive=True):
	print(filename)
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			if 'paths' in fileObj:
				paths.update(fileObj['paths'])
			if 'definitions' in fileObj:
				defin.update(fileObj['definitions'])
		except yaml.YAMLError as exc:
			print(exc)

out = {}
with open(metaFilePath, "r") as metaFile:
	try:
		out = yaml.load(metaFile)
	except yaml.YAMLError as exc:
		print(exc)
		
out['paths'].update(paths)
out['definitions'].update(defin)

with open('out.yaml', 'w') as outfile:
	yaml.dump(out, outfile, default_flow_style=False)
