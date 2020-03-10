
import yaml
import sys

def dereferenceAll(obj, parent):
    #print(breadCrumb)
    try:
        if type(obj) is dict:
            for fieldStr in obj:
                #print(fieldStr)
                if(fieldStr == '$ref'):
                    refPath = obj[fieldStr].split('/')[1:]
                    refObj = parent
                    for refPart in refPath:
                        if refPart in refObj:
                            refObj = refObj[refPart]
                        else:
                            raise Exception('Schema not found ' + obj[fieldStr])

                    refObj = dereferenceAll(refObj, parent)
                    #refObj['title'] = refPath[-1]
                    obj = {**obj, **refObj}
                elif(fieldStr == 'allOf'):
                    comboObj = {'properties': {}, 'type': 'object'}
                    for item in obj[fieldStr]:
                        itemObj = dereferenceAll(item, parent)
                        comboObj['properties'] = {**(comboObj['properties']), **(itemObj['properties'])}
                        if 'title' in itemObj:
                            comboObj['title'] = itemObj['title']
                        if 'description' in itemObj:
                            comboObj['description'] = itemObj['description']
                        if 'example' in itemObj:
                            comboObj['example'] = itemObj['example']
                        
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