#! /usr/bin/env python

# --------------------------------------------READ ME-------------------------------------------------------
# Run this script to combine all the pieces of the the BrAPI specification into a single swagger file.
# ----------------------------------------------------------------------------------------------------------


import yaml
import glob
import sys
import os
import dereferenceAll


def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

def go(rootPaths, metaFilePath = './swaggerMetaData.yaml'):
    paths = {}
    defin = {'schemas': {}, 'parameters': {}, 'responses': {}, 'securitySchemes': {}}
        
    outFilePath = rootPaths[0] + '/brapi_openapi.yaml'
    if os.path.exists(outFilePath):
        os.remove(outFilePath)
        
    filenames = glob.glob(rootPaths[0] + '/**/*.yaml', recursive=True)
    for rootPath in rootPaths[1:]:
        filenames.extend(glob.glob(rootPath + '/**/*.yaml', recursive=True))
    
    for filename in filenames:
        #print(filename)
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
    
    out = dereferenceAll.dereferenceAllOfClause(out, out)
    
    with open(outFilePath, 'w') as outfile:
        print(outFilePath)
        yaml.dump(out, outfile, default_flow_style=False, width=float("inf"), Dumper=noalias_dumper)
    
yaml.add_representer(str, str_presenter)
noalias_dumper = yaml.dumper.SafeDumper
noalias_dumper.ignore_aliases = lambda self, data: True

rootPaths = []
metaFilePath = '.' + '/swaggerMetaData.yaml'
if len(sys.argv) > 1 :
    rootPaths = sys.argv[1:]
    metaFilePath = rootPaths[0] + '/swaggerMetaData.yaml'
else:
    print('need at least one root directory')
    exit(1)
    
go(rootPaths, metaFilePath)

