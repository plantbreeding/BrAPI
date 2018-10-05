#! /usr/bin/env python

import yaml
import glob
import sys


def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)




rootPath = '.'
metaFilePath = './swaggerMetaData.yaml'
if len(sys.argv) > 1 :
    rootPath = sys.argv[1];
if len(sys.argv) > 2 :
    metaFilePath = sys.argv[2];

paths = {}
defin = {'schemas': {}, 'parameters': {}, 'responses': {}, 'securitySchemes': {}}

for filename in glob.iglob(rootPath + '/**/*.yaml', recursive=True):
    print(filename)
    with open(filename, "r") as stream:
        try:
            fileObj = yaml.load(stream)
            if 'paths' in fileObj:
                paths.update(fileObj['paths'])
            if 'components' in fileObj:
                
                if 'schemas' in fileObj['components']:
                    defin['schemas'].update(fileObj['components']['schemas'])
                
                if 'parameters' in fileObj['components']:
                    defin['parameters'].update(fileObj['components']['parameters'])
                
                if 'responses' in fileObj['components']:
                    defin['responses'].update(fileObj['components']['responses'])
                
                if 'securitySchemes' in fileObj['components']:
                    defin['securitySchemes'].update(fileObj['components']['securitySchemes'])
                    
        except yaml.YAMLError as exc:
            print(exc)

out = {}
with open(metaFilePath, "r") as metaFile:
    try:
        out = yaml.load(metaFile)
    except yaml.YAMLError as exc:
        print(exc)
        
out['paths'].update(paths)
out['components'].update(defin)

with open('brapi_openapi.yaml', 'w') as outfile:
    yaml.dump(out, outfile, default_flow_style=False, width=float("inf"))
