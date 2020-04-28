#! /usr/bin/env python

# --------------------------------------------READ ME-------------------------------------------------------
# This script is designed to search a Swagger YAML document for a generic set of criteria. 
# Modify the search() method as needed to locate different objects and circumstances within the Swagger doc.
# Run combineSwagger.py first to generate a complete swagger document for BrAPI.
# ----------------------------------------------------------------------------------------------------------


import yaml
import json
import sys
import re
import dereferenceAll

def go(filePath = './brapi_openapi.yaml'):
    fileObj = dereferenceAll.dereferenceBrAPI(filePath)
    searchList = transform(fileObj)
    search(searchList)
    
def transform(fileObj):
    returnList = []
    if('paths' in fileObj):
        for path in fileObj['paths']:
            isBasePath = re.fullmatch('^/[a-z]+$', path)
            if isBasePath and 'get' in fileObj['paths'][path]:
                if 'parameters' in fileObj['paths'][path]['get']:
                    item = {'path': path, 'params': fileObj['paths'][path]['get']['parameters']}
                else:
                    print('ERROR!!!!')
                returnList.append(item)
            
    return returnList
                
                
def search(searchList):
    for item in searchList:
        dbid = mapPathToDbId(item['path'])
        found = False
        for param in item['params']:
            if param['name'] == dbid:
                found = True
                break
        if not found:
            print(dbid)


def mapPathToDbId(path):
    ## Special cases because English is difficult
    if path.startswith('/attributevalues'):
            return 'attributeValueDbId'
    elif path.startswith('/breedingmethods'):
            return 'breedingMethodDbId'
    elif path.startswith('/callsets'):
            return 'callSetDbId'
    elif path.startswith('/crosses'):
            return 'crossDbId'
    elif path.startswith('/plannedcrosses'):
            return 'plannedCrossDbId'
    elif path.startswith('/crossingprojects'):
            return 'crossingProjectDbId'
    elif path.startswith('/observationunits'):
            return 'observationUnitDbId'
    elif path.startswith('/people'):
            return 'personDbId'
    elif path.startswith('/referencesets'):
            return 'referenceSetDbId'
    elif path.startswith('/seedlots'):
            return 'seedLotDbId'
    elif path.startswith('/studies'):
            return 'studyDbId'
    elif path.startswith('/variables'):
            return 'observationVariableDbId'
    elif path.startswith('/variantsets'):
            return 'variantSetDbId'
    else:
        rootPath = path.split('/')[1]        
        if rootPath[-1] == 's':
            rootPath = rootPath[:-1]
        return rootPath + 'DbId'    

if len(sys.argv) > 1 :
    go(sys.argv[1])
else:
    go()