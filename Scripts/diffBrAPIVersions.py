#! /usr/bin/env python

import sys
import re

def go():
    lowerVersionFilePath = './Specification/brapi_openapi.yaml'
    higherVersionFilePath = './Specification/brapi_openapi.yaml'
    if len(sys.argv) > 2 :
        lowerVersionFilePath = sys.argv[1];
        higherVersionFilePath = sys.argv[2];
    else:
        print('Two files needed to diff')
        exit(1)
    
    lowerVersionFile = {}
    higherVersionFile = {}
    
    with open(lowerVersionFilePath, "r") as stream:
        try:
            lowerVersionFile = yaml.load(stream)
            stream.close()
        except yaml.YAMLError as exc:
            print(exc)
    
    with open(higherVersionFilePath, "r") as stream:
        try:
            higherVersionFile = yaml.load(stream)
            stream.close()
        except yaml.YAMLError as exc:
            print(exc)
            
    dereferenceAll(lowerVersionFile)
    dereferenceAll(higherVersionFile)
    
    pathsToDiff = comparePaths(lowerVersionFile, higherVersionFile)
    compareParams(pathsToDiff, lowerVersionFile, higherVersionFile)
    compareResults(pathsToDiff, lowerVersionFile, higherVersionFile)
    
def comparePaths(lowerVersionFile, higherVersionFile):
    print('comparing paths')
    
def compareParams(pathsToDiff, lowerVersionFile, higherVersionFile):
    print('comparing params')
    
def compareResults(pathsToDiff, lowerVersionFile, higherVersionFile):
    print('comparing results objects')
    
go()