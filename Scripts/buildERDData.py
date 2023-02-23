#! /usr/bin/env python

import yaml
import sys
import json
import dereferenceAll
import os

def buildERDDiagram(specPath):
    with open(specPath + '/brapi_openapi.yaml', "r") as stream:
        try:
            fullBrAPI = yaml.load(stream)
            stream.close()
        except yaml.YAMLError as exc:
            stream.close()

    classes = []
    
    if('components' in fullBrAPI):
        if('schemas' in fullBrAPI['components']):
            x = 0
            for schema in fullBrAPI['components']['schemas']:
                if('x-brapi-metadata' in fullBrAPI['components']['schemas'][schema] and fullBrAPI['components']['schemas'][schema]['x-brapi-metadata']['primaryModel']):
                    schemaObj = fullBrAPI['components']['schemas'][schema]
                    attributes = []
                    if('properties' in schemaObj):
                        attributes = list(schemaObj['properties'].keys())
                    classObj = {'x': x, 'y':0, 'width': 150, 'classname': schema, 'attributes': attributes}
                    x = x + 200
                    classes.append(classObj)                    
                            
    return classes                    

def buildERDDiagramFile(specPath):
    fileContent = {}
    ## For each BrAPI Module
    for module in next(os.walk(specPath))[1]:
        if module[:5] == 'BrAPI':
            print(specPath + module + '/')
            moduleObj = buildERDDiagram(specPath + module + '/')
            fileContent.update({module: moduleObj})
    
    fileName = specPath + '/ERDDiagram.json'
    with open(fileName, 'w') as outfile:
        json.dump(fileContent, outfile, indent=4, sort_keys=True)
        print("fileName - " + fileName)

## Path to BrAPI spec repo. Should end in /Specification/
rootPath = '.'
if len(sys.argv) > 1 :
    rootPath = sys.argv[1];

if rootPath[-1:] != '/':
    rootPath = rootPath + '/'

buildERDDiagramFile(rootPath)
