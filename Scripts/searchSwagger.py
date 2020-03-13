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
            item = {'dataTypes':['application/json'], 'service': path[1:], 'methods': [], 'versions':['2.0'] }
            for method in fileObj['paths'][path]:
                item['methods'].append(method)
            returnList.append(item)
            
    return returnList
                
                
def search(searchList):
    print(json.dumps({'result': {'calls': searchList}}))




if len(sys.argv) > 1 :
    go(sys.argv[1])
else:
    go()