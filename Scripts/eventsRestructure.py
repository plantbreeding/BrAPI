#! /usr/bin/env python

## Usage
## py eventsRestructure.py 

import requests
import json
import sys
import re
import os
    
def go():
    outPath = sys.argv[1]
    
    events = []
    testURL = "https://cassavabase.org/brapi/v2/events?pageSize=100&page=0"
    print("waiting for server")
    response = requests.get(testURL)
    print("download complete")
    rawEvents = response.json()
        
    for rawEvent in rawEvents["result"]["data"]:
        
        eventType = getEventType(rawEvent["eventType"])
        eventDesc = getEventDescription(rawEvent["eventType"])
        date = getEventDate(rawEvent["eventType"], rawEvent["date"], rawEvent["additionalInfo"]["eventCreateDate"])
        eventParams = getEventParameters(rawEvent["eventType"])
        
        newEvent = {
            "additionalInfo": rawEvent["additionalInfo"],
            "date": date,
            "eventDbId": str(rawEvent["eventDbId"]),
            "eventDescription": eventDesc,
            "eventParameters": eventParams,
            "eventType": eventType,
            "eventTypeDbId": rawEvent["eventTypeDbId"],
            "observationUnitDbIds": [ str(rawEvent["observationUnitDbIds"][0]), str(rawEvent["observationUnitDbIds"][1]), "...", str(rawEvent["observationUnitDbIds"][-2]), str(rawEvent["observationUnitDbIds"][-1]) ],
            "studyDbId": str(rawEvent["studyDbId"]),
            "studyName": rawEvent["additionalInfo"]["studyName"]
        }
        events.append(newEvent)
            
    filename = outPath + 'CassavaBaseEventsExample.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as outfile:
        json.dump(events, outfile, indent=4, sort_keys=True)

def getEventType(eventTypeString):
    eventTypeDict = {
        'Hormone treatment': 'other',
        'hormone treatment': 'other',
        'Light treatment': 'other',
        'Weeding': 'weeding', 
        'fertilizer': 'fertilizer',
        'Fertilizer': 'fertilizer', 
        'Fungicide': 'chemicals', 
        'Herbicide': 'chemicals', 
        'herbicide': 'chemicals'
    }
    
    return eventTypeDict.get(eventTypeString, 'other')

def getEventDescription(eventTypeString):
    eventTypeDict = {
        'Hormone treatment': 'Hormone treatment applied to select plots',
        'hormone treatment': 'Hormone treatment applied to select plots',
        'Light treatment': 'Light treatment applied to select plots',
        'Weeding': 'Basic weeding performed', 
        'fertilizer': 'Fertilizer applied to select plots',
        'Fertilizer': 'Fertilizer applied to select plots', 
        'Fungicide': 'Fungicide applied to select plots', 
        'Herbicide': 'Herbicide applied to select plots', 
        'herbicide': 'Herbicide applied to select plots'
    }
    
    return eventTypeDict.get(eventTypeString, '')

def getEventParameters(eventTypeString):
    eventTypeDict = {
        'Hormone treatment': [{"name": "chemical_applic_material", "code": "CHCD", "unit": "code", "value": "CH102"}, {"name": "chemical_applic_name", "code": "CH_NAME", "unit": "text", "value": "Ethylene"}],
        'hormone treatment': [{"name": "chemical_applic_material", "code": "CHCD", "unit": "code", "value": "CH101"}, {"name": "chemical_applic_name", "code": "CH_NAME", "unit": "text", "value": "Ethephon"}],
        'Light treatment': [{"name": "light_intensity", "code": "", "unit": "cd", "value": "2.5"}],
        'Weeding':  [], 
        'fertilizer': [{"name": "fertilizer_material", "code": "FECD", "unit": "code", "value": "FE002"}, {"name": "fertiliz_app_name", "code": "FECD_NAME", "unit": "Text", "value": "Ammonium sulfate"}],
        'Fertilizer': [{"name": "fertilizer_material", "code": "FECD", "unit": "code", "value": "FE900"}, {"name": "fertiliz_app_name", "code": "FECD_NAME", "unit": "Text", "value": "Generic fertilizer"}], 
        'Fungicide': [{"name": "chemical_applic_material", "code": "CHCD", "unit": "code", "value": "CH051"}, {"name": "chemical_applic_name", "code": "CH_NAME", "unit": "text", "value": "Captan [Fungicide]"}],
        'Herbicide': [{"name": "chemical_applic_material", "code": "CHCD", "unit": "code", "value": "CH001"}, {"name": "chemical_applic_name", "code": "CH_NAME", "unit": "text", "value": "Alachlor (Lasso), Metolachlor (Dual) [Herbicide]"}], 
        'herbicide': [{"name": "chemical_applic_material", "code": "CHCD", "unit": "code", "value": "CH012"}, {"name": "chemical_applic_name", "code": "CH_NAME", "unit": "text", "value": "Glyphosate [Herbicide]"}]
    }
    
    return eventTypeDict.get(eventTypeString, [])

def getEventDate(eventType, eventDateArray, eventCreateDate):
    dateObj = {"startDate": None, "endDate": None, "discreteDates": []}
    
    eventDateArray = [x.replace('T000000', 'T00:00:00.000') for x in eventDateArray if x != '']
    eventCreateDate = eventCreateDate.replace(' ', 'T')
    
    if len(eventDateArray)>0:
        dateObj["discreteDates"] = eventDateArray
    else:
        dateObj["discreteDates"].append(eventCreateDate)
    
    return dateObj 
    
    
go()