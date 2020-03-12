#! /usr/bin/env python

## Usage
## diffBrAPIVersions.py [-d][-m][-a][-v] lowerVersionFilePath higherVersionFilePath > outputFilePath

import sys
import re
import yaml
from dereferenceAll import dereferenceBrAPI

sep = '|'
    
def go():
    optionStr = ''
    lowerVersionFilePath = ''
    higherVersionFilePath = ''
    
    if len(sys.argv) > 3 :
        optionStr = sys.argv[1]
        lowerVersionFilePath = sys.argv[2]
        higherVersionFilePath = sys.argv[3]
    elif len(sys.argv) > 2 :
        lowerVersionFilePath = sys.argv[1]
        higherVersionFilePath = sys.argv[2]
    else:
        print('Two files needed to diff')
        exit(1)
    
    options = parseOptions(optionStr)
    lowerVersionFile = dereferenceBrAPI(lowerVersionFilePath)
    higherVersionFile = dereferenceBrAPI(higherVersionFilePath)
    
    deletedDeprecatedPaths, deletedPaths, modifiedPaths, addedPaths = comparePaths(lowerVersionFile, higherVersionFile)
    compareParams(modifiedPaths, lowerVersionFile, higherVersionFile)
    compareResults(modifiedPaths, lowerVersionFile, higherVersionFile)
    
    printResults(deletedDeprecatedPaths, deletedPaths, modifiedPaths, addedPaths, options)
    
def printResults(deletedDeprecatedPaths, deletedPaths, modifiedPaths, addedPaths, options):
    print(len(deletedPaths) + len(deletedDeprecatedPaths), 'endpoints deleted')
    print(len(modifiedPaths), 'endpoints modified')
    print(len(addedPaths), 'endpoints added')
    
    print()
    if options['printDeleted'] :
        print('deleted endpoints')
        for path in sorted(deletedDeprecatedPaths):
            pathSplit = path.split(sep)
            print(pathSplit[1], '\t', pathSplit[0], '\tPreviously deprecated, permanently removed')
        for path in sorted(deletedPaths):
            pathSplit = path.split(sep)
            print(pathSplit[1], '\t', pathSplit[0], '\tFunctionality replaced by XXXX')
    
    print()
    if options['printAdded']:
        print('added endpoints')
        for path in sorted(addedPaths):
            pathSplit = path.split(sep)
            print(pathSplit[1], '\t', pathSplit[0])
            
    print()
    if options['printModified']:
        print('modified endpoints')
        for path in sorted(modifiedPaths.keys()):
            pathSplit = path.split(sep)
            msg = pathSplit[1] + '\t' + pathSplit[0] + '\t%d modifications\n'
            total = 0;
            if len(modifiedPaths[path]['addedParams']) > 0:
                msg += '\t\tParameters Added: ' + arrayToString(modifiedPaths[path]['addedParams']) + '\n'
                total += len(modifiedPaths[path]['addedParams'])
            if len(modifiedPaths[path]['deletedParams']) > 0:
                msg += '\t\tParameters Removed: ' + arrayToString(modifiedPaths[path]['deletedParams']) + '\n'
                total += len(modifiedPaths[path]['deletedParams'])
            if len(modifiedPaths[path]['addedReqFields']) > 0:
                msg += '\t\tRequest Object Fields Added: '+ arrayToString(modifiedPaths[path]['addedReqFields']) + '\n'
                total += len(modifiedPaths[path]['addedReqFields'])
            if len(modifiedPaths[path]['deletedReqFields']) > 0:
                msg += '\t\tRequest Object Fields Removed: '+ arrayToString(modifiedPaths[path]['deletedReqFields']) + '\n'
                total += len(modifiedPaths[path]['deletedReqFields'])
            if len(modifiedPaths[path]['addedResponses']) > 0:
                msg += '\t\tResponses Added: '+ arrayToString(modifiedPaths[path]['addedResponses']) + '\n'
                total += len(modifiedPaths[path]['addedResponses'])
            if len(modifiedPaths[path]['deletedResponses']) > 0:
                msg += '\t\tResponses Removed: '+ arrayToString(modifiedPaths[path]['deletedReqFields']) + '\n'
                total += len(modifiedPaths[path]['deletedResponses'])
            if len(modifiedPaths[path]['addedResponseFields']) > 0:
                msg += '\t\tResponse Object Fields Added: '+ arrayToString(modifiedPaths[path]['addedResponseFields']) + '\n'
                total += len(modifiedPaths[path]['addedResponseFields'])
            if len(modifiedPaths[path]['deletedResponseFields']) > 0:
                msg += '\t\tResponse Object Fields Removed: '+ arrayToString(modifiedPaths[path]['deletedResponseFields']) + '\n'
                total += len(modifiedPaths[path]['deletedResponseFields'])
            
            print(msg % (total))
             
def comparePaths(lowerVersionFile, higherVersionFile):
    print()
    print('comparing paths')
    lowerPaths = []
    higherPaths = []
    deletedDeprecatedPaths = []
    deletedPaths = []
    modifiedPaths = {}
    addedPaths = []
    
    for key in lowerVersionFile['paths'].keys():
        for method in lowerVersionFile['paths'][key].keys():
            lowerPaths.append(key + sep + method)
            
    for key in higherVersionFile['paths'].keys():
        for method in higherVersionFile['paths'][key].keys():
            higherPaths.append(key + sep + method)
    
    
    for lowerPath in lowerPaths:
        matchFound = False
        for higherPath in higherPaths:
            if lowerPath == higherPath:
                matchFound = True
                modifiedPaths[lowerPath] = {'key': lowerPath}
                break
        if not matchFound:
            lowerPathSplit = lowerPath.split(sep)
            if 'deprecated' in lowerVersionFile['paths'][lowerPathSplit[0]][lowerPathSplit[1]] and lowerVersionFile['paths'][lowerPathSplit[0]][lowerPathSplit[1]]['deprecated']:
                deletedDeprecatedPaths.append(lowerPath)
            else:
                deletedPaths.append(lowerPath)
    addedPaths = list(set(higherPaths) - set(modifiedPaths.keys()))
    
    return deletedDeprecatedPaths, deletedPaths, modifiedPaths, addedPaths
        
    
def compareParams(pathsToDiff, lowerVersionFile, higherVersionFile):
    print()
    print('comparing params')
    
    for path in pathsToDiff:
        pathSplit = path.split(sep)
        lowerParams = []
        higherParams = []
        if 'parameters' in lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]] and 'parameters' in higherVersionFile['paths'][pathSplit[0]][pathSplit[1]]:
            lowParams = lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]]['parameters']
            for param in lowParams:
                lowerParams.append(param['name'] + sep + param['schema']['type'])
                
            highParams = higherVersionFile['paths'][pathSplit[0]][pathSplit[1]]['parameters']
            for param in highParams:
                higherParams.append(param['name'] + sep + param['schema']['type'])
        else:
            print('Error: Something is missing Parameter?')
            print(lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]])
            print(higherVersionFile['paths'][pathSplit[0]][pathSplit[1]])
            exit(1)
        
        pathsToDiff[path]['addedParams'] = list(set(higherParams) - set(lowerParams))
        pathsToDiff[path]['deletedParams'] = list(set(lowerParams) - set(higherParams))
        
        
        addedFields = []
        deletedFields = []
        if 'requestBody' in lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]] and 'requestBody' in higherVersionFile['paths'][pathSplit[0]][pathSplit[1]]:
            lowerRequestBody = lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]]['requestBody']
            higherRequestBody = higherVersionFile['paths'][pathSplit[0]][pathSplit[1]]['requestBody']
            if 'application/json' in lowerRequestBody['content'] and 'application/json' in higherRequestBody['content']:
                compareObjects(lowerRequestBody['content']['application/json']['schema'], higherRequestBody['content']['application/json']['schema'], addedFields, deletedFields)
            
        pathsToDiff[path]['addedReqFields'] = addedFields
        pathsToDiff[path]['deletedReqFields'] = deletedFields        

def compareResults(pathsToDiff, lowerVersionFile, higherVersionFile):
    print()
    print('comparing results objects')
    
    for path in pathsToDiff:
        pathSplit = path.split(sep)
        
        addedResponses = []
        deletedResponses = []
        addedFields = []
        deletedFields = []
        if 'responses' in lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]] and 'responses' in lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]]:
            lowerResponses = lowerVersionFile['paths'][pathSplit[0]][pathSplit[1]]['responses']
            higherResponses = higherVersionFile['paths'][pathSplit[0]][pathSplit[1]]['responses']
            
            deletedResponses = list(set(lowerResponses.keys()) - set(higherResponses.keys()))
            addedResponses = list(set(higherResponses.keys()) - set(lowerResponses.keys()))
            modifiedResponses = list(set(higherResponses.keys()) & set(lowerResponses.keys()))
            
            for responseCode in modifiedResponses:
                if 'application/json' in lowerResponses[responseCode]['content'] and 'application/json' in higherResponses[responseCode]['content']:
                    lowerResponseSchema = lowerResponses[responseCode]['content']['application/json']['schema']
                    higherResponseSchema = higherResponses[responseCode]['content']['application/json']['schema']
                    if 'properties' in lowerResponseSchema and 'properties' in higherResponseSchema:
                        compareObjects(lowerResponseSchema['properties']['result'], higherResponseSchema['properties']['result'], addedFields, deletedFields)
                    else:
                        compareObjects(lowerResponseSchema, higherResponseSchema, addedFields, deletedFields)
                        
            
        pathsToDiff[path]['addedResponses'] = addedResponses
        pathsToDiff[path]['deletedResponses'] = deletedResponses 
        pathsToDiff[path]['addedResponseFields'] = addedFields
        pathsToDiff[path]['deletedResponseFields'] = deletedFields 

def compareObjects(lowerRequestBody, higherRequestBody, addedFields, deletedFields, fieldPrefix = 'obj.'):
    
    lowerType = lowerRequestBody['type'] 
    higherType = higherRequestBody['type']
    
    if lowerType == higherType:
        if lowerType == 'object':
            if 'properties' in lowerRequestBody and 'properties' in higherRequestBody:
                deleted = list(set(lowerRequestBody['properties'].keys()) - set(higherRequestBody['properties'].keys()))
                added = list(set(higherRequestBody['properties'].keys()) - set(lowerRequestBody['properties'].keys()))
               
                for d in deleted:
                    deletedFields.append(fieldPrefix + d + sep + lowerRequestBody['properties'][d]['type'])
                for a in added:
                    addedFields.append(fieldPrefix + a + sep + higherRequestBody['properties'][a]['type'])
                
                modifiedFields = list(set(higherRequestBody['properties'].keys()) & set(lowerRequestBody['properties'].keys()))
                for field in modifiedFields:
                    compareObjects(lowerRequestBody['properties'][field], higherRequestBody['properties'][field], addedFields, deletedFields, fieldPrefix + field + '.')
                
        elif lowerType == 'array':
            compareObjects(lowerRequestBody['items'], higherRequestBody['items'], addedFields, deletedFields, fieldPrefix + '.')
    else:
        deletedFields.append(fieldPrefix + sep + lowerType)
        addedFields.append(fieldPrefix + sep + higherType)
        
def arrayToString(array):
    string = ''
    for item in array:
        itemSplit = item.split(sep)
        string += itemSplit[0] 
        if len(itemSplit) > 1:
            string += '(' + itemSplit[1] + ')'
        string += ', '
    
    string = string[:-2]
    return string
    
def parseOptions(optionStr):
    options = {'printDeleted': False, 'printModified': False, 'printAdded': False}
    
    if 'd' in optionStr:
        options['printDeleted'] = True
    if 'm' in optionStr:
        options['printModified'] = True
    if 'a' in optionStr:
        options['printAdded'] = True
    if 'v' in optionStr:
        options['printDeleted'] = True
        options['printModified'] = True
        options['printAdded'] = True
        
    return options
    
go()