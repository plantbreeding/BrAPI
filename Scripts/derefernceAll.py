
import yaml
import sys

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
            elif(fieldStr == 'allOf'):
                comboObj = {'properties': {}}
                for item in obj[fieldStr]:
                    itemObj = dereferenceAll(item, parent)
                    comboObj['properties'] = {**(comboObj['properties']), **(itemObj['properties'])}
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
        
    #print(obj)
    return obj


def dereferenceBrAPI(filePath = './brapi_openapi.yaml'):    
    fileObj = {}
    print(filePath)
    with open(filePath, "r") as stream:
        try:
            fileObj = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    fileObj = dereferenceAll(fileObj, fileObj)
    return fileObj;