#! /usr/bin/env python


import yaml

def go():
    
    wholeFilename = './brapi_openapi_3.yaml'
    wholeFileObj = {}
    
    with open(wholeFilename, "r") as stream:
        try:
            wholeFileObj = yaml.load(stream)
            stream.close()
        except yaml.YAMLError as exc:
            print(exc)
            
    for pathStr in wholeFileObj['components']['schemas']:
        #print(pathStr)
        filename = pathStr + '.yaml'
    
        newObj = { 'openapi': '3.0.0', 'info': { 'title': 'BrAPI', 'version': "1.3-oas3"}, 'paths': {}, 'components': {'schemas': {}}}
        newObj['components']['schemas'][pathStr] = wholeFileObj['components']['schemas'][pathStr]
    
        with open('./out/' + filename, 'w') as outfile:
            yaml.dump(newObj, outfile, default_flow_style=False, width=float("inf"))
            
        print(filename)
        
        
        
        
    
go()