#! /usr/bin/env python

import yaml
import glob
import sys

rootPath = '.'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];

swagger = '2.0'
host = 'https://test-server.brapi.org/'
basePath = '/brapi/v1'
info = {}
paths = {}
defin = {}

for filename in glob.iglob(rootPath + '/**/*.yaml', recursive=True):
	print(filename)
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			info.update(fileObj['info'])
			paths.update(fileObj['paths'])
			defin.update(fileObj['definitions'])
		except yaml.YAMLError as exc:
			print(exc)

out = {'swagger': swagger,
	'host': host,
	'basePath': basePath,
	'info': info,
	'paths': paths,
	'definitions' : defin}

with open('out.yaml', 'w') as outfile:
	yaml.dump(out, outfile, default_flow_style=False)
