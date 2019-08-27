#! /usr/bin/env python

import sys
import glob
import re
from spellchecker import SpellChecker

def go():
    rootPath = './Specification/'
    if len(sys.argv) > 1 :
        rootPath = sys.argv[1];
    if(rootPath[-1] == '/'):
        rootPath = rootPath + '**/*.yaml'
        
    for filename in glob.iglob(rootPath, recursive=True):
        lineNumber = 0
        errorLines = []
        with open(filename, "r") as stream:
            lines = stream.readlines()
            for line in lines:
                lineNumber += 1
                words = parseLine(line)
                unknownWords = spell.unknown(words)
                                    
                if len(unknownWords) > 0:
                    errorMsg = ''
                    for unknownWord in unknownWords:
                         if re.match('[0-9a-f]{8}', unknownWord) is None:
                             errorMsg = errorMsg + unknownWord + ', '
                    if len(errorMsg) > 0:
                        errorLines.append('line ' + str(lineNumber) + ' - ' + errorMsg[:-2])
        if len(errorLines) > 0:
            print('Error in: ', filename)
            for errorLine in errorLines:
                print(errorLine)

def parseLine(line):
    words = splitPattern.split(line)
    words = list(filter(
        lambda x: len(x) > 2, words
    ))
    output = []
    for word in words:
        output.extend(camel_case_split(word))
    #print(words)
    return(output)

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z0-9])|$)', identifier)
    return [m.group(0) for m in matches]

spell = SpellChecker()
spell.word_frequency.load_words([
    #tech
    'json',
    'brapi',
    'openapi',
    'enum',
    '$ref',
    'http',
    'https',
    'wsmime',
    'github',
    'metadata',
    'url',
    'date-time',
    'timestamp',
    'wiki',
    'wikipedia',
    'desc',
    'href',
    'apiary',
    'csv',
    'tsv',
    'flapjack',
    'debug',
    'async',
    #plant
    'germplasm',
    'tomatillo',
    'multi-crop',
    'pui',
    'peco',
    'envo',
    'phenotyping',
    'agronomy',
    'authorships',
    'bioinformatics',
    'plantbreeding',
    'genotyping',
    'orcid',
    'centimeter',
    #fun
    'coladas'])
splitPattern = re.compile('[\s\'\.\-\\"`:;/,_=^@<>{}()\[\]]+')  
go()