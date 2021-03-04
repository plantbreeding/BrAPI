#! /usr/bin/env python

import sys
import glob
import re
import os
from spellchecker import SpellChecker

def go():
    rootPath = './Specification/'
    exitOnFail = False
    
    spell = SpellChecker()
    spell.word_frequency.load_words(['$ref', 'ss+hhmm'])
    spell.word_frequency.load_text_file(os.path.dirname(os.path.realpath(__file__)) + '/checkSpellingDictionary.txt')
    
    if len(sys.argv) > 1 :
        rootPath = sys.argv[1];
    if len(sys.argv) > 2 :
        exitOnFail = sys.argv[2] == '-f';            
    if(rootPath[-1] == '/'):
        rootPath = rootPath + '**/*.yaml'
    
    print('Spell checking ' + rootPath)
    for filename in glob.iglob(rootPath, recursive=True):
        lineNumber = 0
        errorLines = []
        with open(filename, "r") as stream:
            lines = stream.readlines()
            for line in lines:
                lineNumber += 1
                if(lineNumber == 6):
                    continue
                words = parseLine(line)
                unknownWords = spell.unknown(words)
                                    
                if len(unknownWords) > 0:
                    errorMsg = ''
                    for unknownWord in unknownWords:
                        errorMsg = errorMsg + unknownWord + ', '
                    if len(errorMsg) > 0:
                        errorLines.append('line ' + str(lineNumber) + ' - ' + errorMsg[:-2])
        if len(errorLines) > 0:
            print('Error in: ', filename)
            for errorLine in errorLines:
                print(errorLine)
            if(exitOnFail):
                exit(1)

def parseLine(line):
    splitPattern = re.compile("([^\w\d]|[_])+")  
    words = splitPattern.split(line)
    # Split Camel Case words 
    wordsCamel = []
    for word in words:
        wordsCamel.extend(camel_case_split(word))
    words = wordsCamel
    # Remove short words
    words = list(filter(lambda x: len(x) > 2, words))
    # Remove all caps (assume acronym)
    words = list(filter(lambda x: re.match(r'^[A-Z]*$', x)  is None, words))
    # Remove 8 character hexidecimal (assume DbId)
    words = list(filter(lambda x: re.match(r'^[0-9A-F]{8}$|^[0-9a-f]{8}$', x) is None, words))
    #print(words)
    return(words)

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z0-9])|$)', identifier)
    return [m.group(0) for m in matches]


##splitPattern = re.compile("(?:\\\\n|[\s\'\.\-\\\"\*`:;/,_=^@#<>{}()\[\]])+")
go()