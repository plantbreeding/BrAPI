
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
        print(obj)
        raise ex
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