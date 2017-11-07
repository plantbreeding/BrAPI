## Variable search [/brapi/v1/variables-search]
Scope: CORE.
Status: ACCEPTED.

Search for a list of Observation Variables. An Observation Variable is defined as the unique combination of a Trait being observed, a Method used for the observation and a Scale to define the observation (ie units). 

All of the parameters in the search request object are optional. Any missing input parameter in the search request object is ignored with no default value. 
Each input parameter present in the request object is be used to restrict and filter the data (AND filter). 
Each element within the array of a single parameter is used to identify additional data (OR filter).

SQL Implementation Example:
select * from variables where 
(observationVariableDbId = "obs-variable-id1"   OR   observationVariableDbId = "obs-variable-id2")
AND 
(methodDbId = "method-1"   OR   methodDbId = "method-2")
AND 
(scaleDbId = "scale-1"   OR   scaleDbId = "scale-2")


### Variable search [POST]
+ Parameters
   + observationVariableDbIds (optional, array, `["obs-variable-id1", "obs-variable-id2"]`) ... Internal ID used to identify an Observation Variable within an arbitrary data store 
   + ontologyDbIds (optional, array, `["CO_334:0100632"]`) ... Internal ID used to identify an Observation Variable within the shared ontology data store
   + ontologyXrefs (optional, array, `["CO:123", "CO:456"]`) ... External reference ID used to identify an Observation Variable within the shared ontology data store
   + methodDbIds (optional, array, `["method-1", "method-2"]`) ... The ID associated with a particular method
   + scaleDbIds (optional, array, `["scale-1", "scale-2"]`) ... The ID associated with a particular scale
   + names (optional, array, `["caro_spectro"]`) ... The human readable name of an Observation Variable
   + datatypes (optional, array, `["numeric"]`) ... The type of data being observed
   + traitClasses (optional, array, `["Phenological", "Physiological"]`) ... The class of trait being observed
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `10`) ... Which result page is requested

+ Request (application/json)

        {
            "page": 0,
            "pageSize": 2,
            "observationVariableDbIds" : ["obs-variable-id1", "obs-variable-id2"],
            "ontologyXrefs" : ["CO:123", "CO:456"],
            "ontologyDbIds" : ["CO_334:0100632"],
            "methodDbIds" : ["method-1", "method-2"],
            "scaleDbIds" : ["scale-1", "scale-2"],
            "names" : ["caro_spectro"],
            "datatypes" : ["numeric"],
            "traitClasses" : ["Phenological", "Physiological"]
        }

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 300,
                    "totalPages": 100
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [{
                    "observationVariableDbId": "CO_334:0100632",
                    "name": "CT_M_C",
                    "ontologyDbId": "CO_334",
                    "ontologyName": "Cassava",
                    "trait": {
                        "traiDbId": "CO_334:0100630",
                        "name": "Canopy temperature"
                    },
                    "method": null,
                    "scale": null,
                    "defaultValue": null
                }, {
                  "observationVariableDbId": "CO_334:0100622",
                  "name": "caro_spectro",
                  "ontologyDbId": "CO_334",
                  "ontologyName": "Cassava",
                  "synonyms": ["Carotenoid content by spectro"],
                  "contextOfUse": ["Trial evaluation", "Nursery evaluation"],
                  "growthStage": "mature",
                  "status": "recommended",
                  "xref": "TL_455:0003001",
                  "institution": "",
                  "scientist": "",
                  "submissionTimestamp": "2016-05-13T23:21:56+0100",
                  "language": "EN",
                  "crop": "Cassava",
                  "trait": {
                      "traitDbId": "CO_334:0100620",
                      "name": "Carotenoid content",
                      "class": "physiological trait",
                      "description": "Cassava storage root pulp carotenoid content",
                      "synonyms": ["carotenoid content measure"],
                      "mainAbbreviation": "CC",
                      "alternativeAbbreviations": ["CCS"],
                      "entity": "root",
                      "attribute": "carotenoid",
                      "status": "recommended",
                      "xref": "TL_455:0003023"
                  },
                  "method": {
                      "methodDbId": "CO_334:0010320",
                      "name": "Visual Rating:total carotenoid by chart_method",
                      "class": "Estimation",
                      "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                      "formula": null,
                      "reference": null
                  },
                  "scale": {
                      "scaleDbId": "CO_334:0100526",
                      "name": "ug/g",
                      "datatype": "Numeric",
                      "decimalPlaces": 2,
                      "xref": null,
                      "validValues": {
                          "min": 1,
                          "max": 3,
                          "categories": ["1=low", "2=medium", "3=high"]
                      }
                  },
                  "defaultValue": null
                }]
            }
        }
