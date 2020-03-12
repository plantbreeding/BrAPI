#! /usr/bin/env python

# --------------------------------------------READ ME-------------------------------------------------------
# This script is designed to search a Swagger YAML document for a generic set of criteria. 
# Modify the search() method as needed to locate different objects and circumstances within the Swagger doc.
# Run combineSwagger.py first to generate a complete swagger document for BrAPI.
# ----------------------------------------------------------------------------------------------------------


import yaml
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
            for method in fileObj['paths'][path]:
                #if method == 'get' and not path.startswith('/search') and path[-1] == '}':
                item = {'path': path, 'method': method}
                returnList.append(item)
                
    return returnList
                
                
def search(searchList):
    hits = set([])
    for item in searchList:
        path = item['path']
        method = item['method']
        
        isBasePath = re.fullmatch('^/[a-z]+$', path)
        isDbIdPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}$', path)
        isDbIdExtraPath = re.fullmatch('^/[a-z]+/\{[a-zA-Z]+}/[a-z]+$', path)
        isTablePath = re.fullmatch('^/[a-z]+/table$', path)
        isVendorPath = re.fullmatch('^/vendor/.+$', path)
        isSearchPostPath = re.fullmatch('^/search/[a-z]+$', path)
        isSearchGetPath = re.fullmatch('^/search/[a-z]+/{searchResultsDbId}$', path)
        
        
        if isBasePath: 
            if method == 'get':
                #filter
                hits.add(1)
            elif method == 'post':
                #new stuff
                hits.add(2)
            elif method == 'put':
                #update list
                hits.add(3)
        elif isDbIdPath:
            if method == 'get':
                #filter
                hits.add(4)
            elif method == 'post':
                #new stuff
                hits.add(5)
                print(' ----5--- ' + method + path)
            elif method == 'put':
                #update list
                hits.add(6)
        elif isDbIdExtraPath:
            if method == 'get':
                #filter
                hits.add(7)
            elif method == 'post':
                #new stuff
                hits.add(8)
            elif method == 'put':
                #update list
                hits.add(9)
        elif isTablePath:
            #table
            hits.add(10)
        elif isVendorPath:
            #vendor
            if method == 'get':
                hits.add(11)
            elif method == 'post':
                hits.add(12)
        elif isSearchPostPath:
            #seach post
            hits.add(13)
        elif isSearchGetPath:
            #seach get
            if method == 'get':
                hits.add(14)
            elif method == 'post':
                hits.add(15)
                print(' ---15--- ' + method + path)
        else:
            print(method + path)
        
    print(hits)

if len(sys.argv) > 1 :
    go(sys.argv[1])
else:
    go()