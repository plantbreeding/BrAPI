#! /usr/bin/env python

import sys
import glob
import re
from spellchecker import SpellChecker

def go():
    rootPath = './Specification/'
    exitOnFail = False
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

spell = SpellChecker()
spell.word_frequency.load_words([
    #tech
    'brapi',
    'json', 'csv', 'tsv', 'flapjack', 'jpg', 'svg', 'postgres', 'md5sum', 'md5checksum', 'fileadmin', 'pdfs', 'xlsx',
    'http', 'https', 'url', 'href', 'html', 'webpage', 'www', 'wiews',
    'openapi', 'apiary', 'github', 'swaggerhub', 'ga4gh', 
    'brapicore', 'brapiphenotyping', 'brapigenotyping', 'brapigermplasm',
    'enum', 'wsmime', 'date-time', 'timestamp', 'uuid',
    '$ref', 'metadata', 'desc',
    'wiki', 'wikipedia',
    'uppercase', 'lowercase', 'concatenated', 'whitespace',
    'xref', 'xrefs', 'xmlns', 'foaf',
    'preprocessing','debug', 'async', 'upload', 'uploaded', 'imagecontent', 'unpaginated',
    '2px', '5px', '10px', '20px', '#ddd',
    'thh', 'ss+hhmm', 'yyyy', 'o8601', 'timezone', 's84', 't18',
    #plant
    'germplasm', 'genebank', 'genebanks',
    'multi-crop', 'subblock',
    'pui', 'peco', 'envo', 'puid', 'r001', 'geodetic', 'georeference', 'georeferencing',
    'phenotyping', 'genotyping', 'agronomy', 'phenological', 'agronomical',
    'authorships', 'orcid',
    'bioinformatics', 'plantbreeding',
    'centimeter', 'centimeters', 'unphased', 'log10',
    'mcpd', 'ncbi', 'miappe', 'ebi', 'biosample', 'biosamples', 'inra', 'gnpis', 'cipos', 'ciend', 'svlen', 'bioversity',
    'subtaxa', 'subtaxon', 'subform', 'subvariety', 'infraspecific', 'convar', 'convariety', 'amphiploids', 'aneuploids', 'landrace', 'cryo', 'ruderal', 'shrubland',
    'obo', 'rdf', 'obolibrary', 'ontologies', 'vcf', 'hapmap',
    'carotenoid', 'pipet', 'plateless', 'indel', 'parent1', 'parent2',
    'Zea', 'mays', 'fructus', 'c2365e900c81a89cf74d83dab60df146', 
    #fun
    'tomatillo', 'hadron', 'coladas', 'townsville'])
splitPattern = re.compile("(?:\\\\n|[\s\'\.\-\\\"\*`:;/,_=^@#<>{}()\[\]])+")  
go()