#! /usr/bin/env python

# --------------------------------------------READ ME-------------------------------------------------------
# This script is designed to search a Swagger YAML document for a generic set of criteria. 
# Modify the search() method as needed to locate different objects and circumstances within the Swagger doc.
# Run combineSwagger.py first to generate a complete swagger document for BrAPI.
# ----------------------------------------------------------------------------------------------------------


import yaml
import sys

def go(filePath = './brapi_openapi.yaml'):    
    fileObj = {}
    print(filePath)
    with open(filePath, "r") as stream:
        try:
            fileObj = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    fileObj = dereferenceAll(fileObj, fileObj)
    searchList = transform(fileObj)
    search(searchList)
    
def transform(fileObj):
    returnList = []
    if('paths' in fileObj):
        for path in fileObj['paths']:
            for method in fileObj['paths'][path]:
                obj = {}
                obj['path'] = path
                obj['method'] = method
                if 'deprecated' in fileObj['paths'][path][method]:
                    obj['deprecated'] = fileObj['paths'][path][method]['deprecated']
                else:
                    obj['deprecated'] = False
                    
                if 'description' in fileObj['paths'][path][method]:
                    obj['description'] = fileObj['paths'][path][method]['description']
                else:
                    obj['description'] = ''
                    
                if 'parameters' in fileObj['paths'][path][method]:
                    obj['parameters'] = fileObj['paths'][path][method]['parameters']
                else:
                    obj['parameters'] = []
                    
                if 'requestBody' in fileObj['paths'][path][method]:
                    obj['requestBody'] = fileObj['paths'][path][method]['requestBody']
                else:
                    obj['requestBody'] = {}
                    
                if 'responses' in fileObj['paths'][path][method]:
                    if '200' in fileObj['paths'][path][method]['responses']:
                        if 'content' in fileObj['paths'][path][method]['responses']['200']:
                            if 'application/json' in fileObj['paths'][path][method]['responses']['200']['content']:
                                obj['response'] = fileObj['paths'][path][method]['responses']['200']['content']['application/json']
                            else:
                                print('Warning: ' + method + path + ' is missing response json')
                        else:
                            print('Warning: ' + method + path + ' is missing response content')
                    else:
                        print('Warning: ' + method + path + ' is missing 200 response')
                    
                returnList.append(obj)
                
    return returnList
                
                
def search(searchList):
    for item in searchList:
        #print(item['response']['schema'])
        #print(item['path'])
        if not item['deprecated']:
            
            for parameter in item['parameters']:
                paramName = parameter['name']
                if (paramName[-4:] == 'DbId' 
                        or paramName[-5:] == 'DbIds' 
                        or paramName[-2:] == 'Id'):
                    allKeys = findAllKeys(item['response']['schema'])
                    if not paramName in allKeys:
                        print(paramName + ' not found in response for ' + item['method'] + item['path'])

def findAllKeys(schema, keys = []):
    if type(schema) is dict:
        for key in schema:
            keys.append(key)
            keys = findAllKeys(schema[key], keys)
    return keys

def dereferenceAll(obj, parent):
    if type(obj) is dict:
        for fieldStr in obj:
            if(fieldStr == '$ref'):
                refPath = obj[fieldStr].split('/')
                refObj = parent
                for refPart in refPath:
                    if refPart in refObj:
                        refObj = refObj[refPart]
                refObj = dereferenceAll(refObj, parent)
                obj = {**obj, **refObj}
            else:
                obj[fieldStr] = dereferenceAll(obj[fieldStr], parent)
        if '$ref' in obj:
            obj.pop('$ref')
    elif type(obj) is list:
        newList = []
        for item in obj:
            newList.append(dereferenceAll(item, parent))
        obj = newList
        
    #print(obj)
    return obj


if len(sys.argv) > 1 :
    go(sys.argv[1])
else:
    go()