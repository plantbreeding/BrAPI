#! /usr/bin/env python

import yaml
import glob
import sys
import json
import requests
from copy import deepcopy
import jsonschema
from jsonschema import validate
import dereferenceAll


def replaceIDs(url):
	newURL = url
	newURL = newURL.replace('{studyDbId}', '1001')
	newURL = newURL.replace('{mapDbId}', 'gm1')
	newURL = newURL.replace('{breedingMethodDbId}', 'bm1')
	newURL = newURL.replace('{germplasmDbId}', '3')
	newURL = newURL.replace('{locationDbId}', '1')
	newURL = newURL.replace('{observationVariableDbId}', 'MO_123:100002')
	newURL = newURL.replace('{traitDbId}', 't1')
	newURL = newURL.replace('{trialDbId}', '101')
	newURL = newURL.replace('{markerDbId}', 'mr02')
	newURL = newURL.replace('{markerProfileDbId}', 'P1')
	newURL = newURL.replace('{linkageGroupName}', '1')
	newURL = newURL.replace('{sampleDbId}', 'sam01')
	newURL = newURL.replace('{vendorPlateDbId}', 'pl1')
	newURL = newURL.replace('{imageDbId}', 'img1')
	newURL = newURL.replace('{listDbId}', 'list1')
	newURL = newURL.replace('{personDbId}', 'person1')
	newURL = newURL.replace('{methodDbId}', 'm1')
	newURL = newURL.replace('{scaleDbId}', 's1')
	newURL = newURL.replace('{traitDbId}', 't1')
	newURL = newURL.replace('{searchResultsDbId}', 'search01')
	return newURL


def postParams(path):
	params = {'pageSize': 2}
	if path == '/vendor/plates':
		params = {
		  "plates": [
		    {
		      "clientPlateDbId": "string",
		      "plateFormat": "string",
		      "sampleType": "string",
		      "samples": [
		        {
		          "column": "1",
		          "concentration": "string",
		          "row": "0",
		          "sampleDbId": "string",
		          "taxonId": {
		            "sourceName": "string",
		            "taxonId": "string"
		          },
		          "tissueType": "string",
		          "volume": "string",
		          "well": "1"
		        }
		      ],
		      "vendorProjectDbId": "string"
		    }
		  ]
		}
	elif path == '/phenotypes':
		params = {
		  "data": [
		    {
		      "observatioUnitDbId": "1",
		      "observations": [
		        {
		          "collector": "string",
		          "observationDbId": "string",
		          "observationTimeStamp": "2018-09-19T15:57:27.903Z",
		          "observationVariableDbId": "MO_123:100002",
		          "observationVariableName": "string",
		          "season": "fall 2011",
		          "value": "string"
		        }
		      ],
		      "studyDbId": "string"
		    }
		  ]
		}
	elif path == '/markers-search' : 
		params['includeSynonyms'] = 'true'
	elif path == '/images':
		params = {
				  "copyright": "Copyright 2019",
				  "description": "BrAPI Logo",
				  "descriptiveOntologyTerms": [ "brapi", "logo" ],
				  "imageFileName": "brapi-logo.svg",
				  "imageFileSize": 3676,
				  "imageHeight": 56,
				  "imageName": "brapiLogo",
				  "imageWidth": 258,
				  "mimeType": "image/svg",
				  "observationDbIds": [ "1", "2" ],
				  "observationUnitDbId": "1",
				  "imageLocation": {
					                    "geometry": {
					                        "type": "Point",
					                        "coordinates": [
					                            - 110.11301,
					                            50.010082
					                        ]
					                    },
					                    "type": "Feature"
					                },
				  "imageTimeStamp": "2011-06-14",
				  "imageURL": "https://brapi.org/assets/images/brapi-logo.svg"
				}
	elif path == '/lists':
		params = {
				  "data": [
				    "string"
				  ],
				  "description": "string",
				  "listName": "string",
				  "listOwnerName": "string",
				  "listOwnerPersonDbId": "string",
				  "listSize": 0,
				  "listSource": "string",
				  "listType": "germplasm"
				}
	elif path == '/lists/{listDbId}/items':
		params = ["1", "2", "3"]
	elif path == '/people':
		params = {
				  "description": "string",
				  "emailAddress": "string",
				  "firstName": "Name",
				  "lastName": "Smith",
				  "mailingAddress": "string",
				  "middleName": "string",
				  "phoneNumber": "string",
				  "userID": "string"
				}
	elif path == '/methods':
		params = {
				  "class": "string",
				  "description": "string",
				  "formula": "string",
				  "methodName": "string",
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "reference": "string"
				}
	elif path == '/scales':
		params = {
				  "dataType": "Code",
				  "decimalPlaces": 0,
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "scaleName": "string",
				  "validValues": {
				    "categories": [
				      "string"
				    ],
				    "max": 0,
				    "min": 0
				  },
				  "xref": "string"
				}
	elif path == '/traits':
		params = {
				  "alternativeAbbreviations": [
				    "string"
				  ],
				  "attribute": "string",
				  "class": "string",
				  "description": "string",
				  "entity": "string",
				  "mainAbbreviation": "string",
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "status": "string",
				  "synonyms": [
				    "string"
				  ],
				  "traitName": "string",
				  "xref": "string"
				}
	elif path == '/studies/{studyDbId}/observationunits':
		params = {
				  "metadata": {},
				  "result": {
				    "commit": "string",
				    "data": [
				      {
				        "observatioUnitDbId": "1",
				        "observations": [
				          {
				            "collector": "string",
				            "observationDbId": "1",
				            "observationTimeStamp": "2018-11-26T22:07:58.096Z",
				            "observationUnitDbId": "1",
				            "observationVariableDbId": "MO_123:100002",
				            "value": "string"
				          }
				        ],
				        "studyDbId": 1001
				      }
				    ],
				    "transactionDbId": "string"
				  }
				}
	elif path == '/studies/{studyDbId}/table':
		params = {
				  "data": [
				    [
				      "1", "2", "3"
				    ]
				  ],
				  "headerRow": [
				    "blockNumber", "plotNumber"
				  ],
				  "observationVariableDbIds": [
				    "MO_123:100002"
				  ]
				}
		 
	return params


def putParams(path):
	params = {'pageSize': 2}
	if path == '/samples':
		params = {
		  "germplasmDbId": "1",
		  "notes": "string",
		  "observationUnitDbId": "1",
		  "plantDbId": None,
		  "plateDbId": "string",
		  "plateIndex": 0,
		  "plotDbId": "1",
		  "sampleDbId": "string",
		  "sampleTimestamp": "2018-09-25T21:07:17.505Z",
		  "sampleType": "string",
		  "studyDbId": "1001",
		  "takenBy": "string",
		  "tissueType": "string"
		}
	elif path == '/studies/{studyDbId}/observationunits':
		params = [
				  {
				    "blockNumber": "string",
				    "entryNumber": "string",
				    "entryType": "string",
				    "germplasmDbId": "2",
				    "observationLevel": "string",
				    "observationUnitDbId": "1",
				    "observationUnitName": "string",
				    "observationUnitXref": [
				      {
				        "id": "string",
				        "source": "string"
				      }
				    ],
				    "observations": [
				      {
				        "germplasmDbId": "2",
				        "germplasmName": "string",
				        "observationDbId": "1",
				        "observationLevel": "string",
				        "observationTimeStamp": "2018-11-26T22:39:48.919Z",
				        "observationUnitDbId": "1",
				        "observationUnitName": "string",
				        "observationVariableDbId": "MO_123:100005",
				        "observationVariableName": "string",
				        "operator": "string",
				        "season": {
				          "season": "string",
				          "seasonDbId": "1",
				          "year": "string"
				        },
				        "studyDbId": "1001",
				        "uploadedBy": "string",
				        "value": "string"
				      }
				    ],
				    "plantNumber": "string",
				    "plotNumber": "string",
				    "positionCoordinateX": "string",
				    "positionCoordinateXType": "LONGITUDE",
				    "positionCoordinateY": "string",
				    "positionCoordinateYType": "LONGITUDE",
				    "replicate": "string",
				    "studyDbId": "1001",
				    "treatments": [
				      {
				        "factor": "string",
				        "modality": "string"
				      }
				    ]
				  }
				]
	elif path == '/studies/{studyDbId}/observations':
		params = {
				  "observations": [
				    {
				      "collector": "string",
				      "observationDbId": "5",
				      "observationTimeStamp": "2018-11-26T20:56:29.814Z",
				      "observationUnitDbId": "1",
				      "observationVariableDbId": "MO_123:100002",
				      "value": "string"
				    }
				  ]
				}
	elif path == '/images/{imageDbId}':
		params = {
				  "copyright": "Copyright 2019",
				  "description": "BrAPI Logo",
				  "descriptiveOntologyTerms": [ "brapi", "logo" ],
				  "imageFileName": "brapi-logo.svg",
				  "imageFileSize": 3676,
				  "imageHeight": 56,
				  "imageName": "brapiLogo",
				  "imageWidth": 258,
				  "mimeType": "image/svg",
				  "observationDbIds": [ "1", "2" ],
				  "observationUnitDbId": "1",
				  "imageLocation": {
					                    "geometry": {
					                        "type": "Point",
					                        "coordinates": [
					                            - 110.11301,
					                            50.010082
					                        ]
					                    },
					                    "type": "Feature"
					                },
				  "imageTimeStamp": "2011-06-14",
				  "imageURL": "https://brapi.org/assets/images/brapi-logo.svg"
				}
	elif path == '/lists/{listDbId}':
		params = {
				  "data": [
				    "string"
				  ],
				  "description": "string",
				  "listName": "string",
				  "listOwnerName": "string",
				  "listOwnerPersonDbId": "string",
				  "listSize": 0,
				  "listSource": "string",
				  "listType": "germplasm"
				}
	elif path == '/people/{personDbId}':
		params = {
				  "description": "string",
				  "emailAddress": "string",
				  "firstName": "Name",
				  "lastName": "Nameson",
				  "mailingAddress": "string",
				  "middleName": "string",
				  "phoneNumber": "string",
				  "userID": "string"
				}
	elif path == '/methods/{methodDbId}':
		params = {
				  "class": "string",
				  "description": "string",
				  "formula": "string",
				  "methodName": "string",
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "reference": "string"
				}
	elif path == '/scales/{scaleDbId}':
		params = {
				  "dataType": "Code",
				  "decimalPlaces": 0,
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "scaleName": "string",
				  "validValues": {
				    "categories": [
				      "string"
				    ],
				    "max": 0,
				    "min": 0
				  },
				  "xref": "string"
				}
	elif path == '/traits/{traitDbId}':
		params = {
				  "alternativeAbbreviations": [
				    "string"
				  ],
				  "attribute": "string",
				  "class": "string",
				  "description": "string",
				  "entity": "string",
				  "mainAbbreviation": "string",
				  "ontologyRefernce": {
				    "documentationLinks": [
				      {
				        "URL": "string",
				        "type": "OBO"
				      }
				    ],
				    "ontologyDbId": "MO_123",
				    "ontologyName": "string",
				    "version": "string"
				  },
				  "status": "string",
				  "synonyms": [
				    "string"
				  ],
				  "traitName": "string",
				  "xref": "string"
				}
	elif path == '/studies/{studyDbId}/layouts' or path == '/studies/{studyDbId}/layout':
		params = {
					"layout": [
				    {
				      "blockNumber": 0,
				      "entryType": "CHECK",
				      "observationUnitDbId": "2",
				      "X": "1",
				      "Y": "1",
				      "positionCoordinateX": "1",
				      "positionCoordinateXType": "LONGITUDE",
				      "positionCoordinateY": "1",
				      "positionCoordinateYType": "LONGITUDE",
				      "replicate": 0
				    }
				  ]
				}
				
		
	return params


def getParams(path):
	params = {'pageSize': 2}
	if path == '/markers-search' : 
		params['includeSynonyms'] = 'true'
	elif path == '/markers':
		params['include'] = 'synonyms'
	elif path == '/germplasm/{germplasmDbId}/pedigree':
		params['includeSiblings'] = 'true'
	return params
