
import yaml
import sys

def findRef(ref, parent):
    refPath = ref.split('/')[1:]
    #print(ref)
    #print(refPath)
    refObj = parent
    for refPart in refPath:
        #print(refPart)
        if refPart in refObj:
            refObj = refObj[refPart]
        else:
            raise Exception('Schema not found ' + refPart)
    
    return refObj

def dereferenceAll(obj, parent):
    #print(breadCrumb)
    try:
        if type(obj) is dict:
            for fieldStr in obj:
                #print(fieldStr)
                if(fieldStr == '$ref'):
                    refObj = dereferenceAll(findRef(obj[fieldStr], parent), parent)
                    #refObj['title'] = refPath[-1]
                    obj = {**obj, **refObj}
                elif(fieldStr == 'allOf'):
                    comboObj = {'properties': {}, 'type': 'object', 'required': []}
                    for item in obj[fieldStr]:
                        itemObj = dereferenceAll(item, parent)
                        comboObj['properties'] = {**(comboObj['properties']), **(itemObj['properties'])}
                        if 'required' in itemObj:
                            comboObj['required'] = list(set(comboObj['required'] + itemObj['required']))
                        if 'title' in itemObj:
                            comboObj['title'] = itemObj['title']
                        if 'description' in itemObj:
                            comboObj['description'] = itemObj['description']
                        if 'example' in itemObj:
                            comboObj['example'] = itemObj['example']
                        if 'x-brapi-metadata' in itemObj:
                            comboObj['x-brapi-metadata'] = itemObj['x-brapi-metadata']
                        
                    obj = comboObj
                else:
                    obj[fieldStr] = dereferenceAll(obj[fieldStr], parent)
            if '$ref' in obj:
                obj.pop('$ref')
        elif type(obj) is list:
            newList = []
            for item in obj:
                newList.append(dereferenceAll(item, parent))
            obj = newList
    except Exception as ex:
        ##print(obj)
        raise ex
    return obj


def dereferenceAllOfClause(obj, parent):
    #print(breadCrumb)
    try:
        if type(obj) is dict:
            for fieldStr in obj:
                #print(fieldStr)
                if(fieldStr == 'allOf'):
                    comboObj = {'properties': {}, 'type': 'object', 'required': []}
                    for item in obj[fieldStr]:
                        itemObj = dereferenceAll(item, parent)
                        
                        if 'properties' in itemObj:
                            comboObj['properties'] = {**(comboObj['properties']), **(itemObj['properties'])}
                        if 'required' in itemObj:
                            comboObj['required'] = list(set(comboObj['required'] + itemObj['required']))
                        if 'title' in itemObj:
                            comboObj['title'] = itemObj['title']
                        if 'description' in itemObj:
                            comboObj['description'] = itemObj['description']
                        if 'example' in itemObj:
                            comboObj['example'] = itemObj['example']
                        if 'x-brapi-metadata' in itemObj:
                            comboObj['x-brapi-metadata'] = itemObj['x-brapi-metadata']
                    
                    if len(comboObj['required']) == 0:
                        comboObj.pop('required')
                    
                    obj = comboObj
                else:
                    obj[fieldStr] = dereferenceAllOfClause(obj[fieldStr], parent)
        elif type(obj) is list:
            newList = []
            for item in obj:
                newList.append(dereferenceAllOfClause(item, parent))
            obj = newList
    except Exception as ex:
        ##print(obj)
        raise ex
    return obj


def dereferenceBrAPI(filePath = './brapi_openapi.yaml', verbose = False):    
    fileObj = {}
    if verbose :
        print(filePath)
    with open(filePath, "r") as stream:
        try:
            fileObj = yaml.load(stream)
            stream.close()
        except yaml.YAMLError as exc:
            stream.close()
            if verbose :
                print(exc)
    
    fileObj = dereferenceAll(fileObj, fileObj)
    return fileObj;