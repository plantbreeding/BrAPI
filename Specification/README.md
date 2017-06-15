FORMAT: 1A

# BrAPI Overview

The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve 
their data to crop breeding applications. It is a <i>shared</i>, <i>open</i> API, to be
used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is
currently in an actively developing state, so now is the time for potential participants to help
shape the specifications to ensure their needs are addressed. The listserve for discussions and 
announcements is at http://mail2.sgn.cornell.edu/cgi-bin/mailman/listinfo/plant-breeding-api .
Additional documentation is in the <a href="https://github.com/plantbreeding/documentation">Github wiki</a>.

### URL structure

API requests are structured as "\<server\>/brapi/v1/", 
where "v1" is the version number of the API, followed by the command.  
Example: /brapi/v1/markerprofiles/2939 

To distinguish between multiple databases or crops available from the same server, include the database or crop name as part of the "\<server\>" identifier. An arbitrary number of levels can be inserted between the domain name and the crops or brapi level, if needed.

Example: superBreedingServer.org/maize/brapi/v1/markerprofiles/2939

### Structure of the response object:

The return objects are encoded in JSON. The response consists of:
+ A "metadata" key containing pagination, status, and file information;
+ A "result" key that can contain:
  + Arbitrary properties; and/or
  + A "data" key containing an array of objects of the same type.


#### The Metadata Key

The metadata key is structured as followed:


````
{
  "metadata" : {
      "pagination" : {
            "totalCount" : 0,
	     "pageSize" : 0,
	     "totalPages" : 0,
	     "currentPage" : 0
	     },
       "status" : [{
                      "code" : "asynchstatus",
	              "message" : "PENDING"
		   }],
       "datafiles" : [/mnt/local/matrix_01.csv,
                      /mnt/local/matrix_02.csv]
	}, . . . 
}
````

+  **pagination**: The pagination object is applicable only When the "data" key contains multiple objects. In this case, the keys "pageSize", "currentPage", "totalCount", "totalPages" contain the appropriate values. Pages are zero indexed, so the first page will be page 0 (zero). (For the user interface, this may be adjusted by adding 1).


+ **status**: The status object contains a list of objects with the keys "code" and "message". If no status is reported, the empty list should be returned.

+ **datafiles**: The datafiles key contains a list of strings. The empty list should be returned if no datafiles are present.

#### Payload

The BRAPI response payload allows for three different types of responses:
+ **master**: In this type of response, the "result" key consists of arbitrary properties without a "data" key; for example, the germplasm/{id} call may contain the following: 
````
{
  "metadata" : {
    "pagination" : {
      "totalCount" : 0,
      "pageSize" : 0,
      "totalPages" : 0,
      "currentPage" : 0
    },
    "status" : [ ],
    "datafiles" : [ ]
  },
  "result" : {
    "typeOfGermplasmStorageCode" : null,
    "pedigree" : null,
    "seedSource" : null,
    "species" : null,
    "subtaxa" : null,
    "biologicalStatusOfAccessionCode" : null,
    "countryOfOriginCode" : null,
    "synonyms" : null,
    "genus" : null,
    "instituteName" : null,
    "subtaxaAuthority" : null,
    "germplasmDbId" : "1",
    "defaultDisplayName" : null,
    "acquisitionDate" : null,
    "donors" : [ {
      "donorGermplasmPUI" : "testdonorid1",
      "donorAccessionNumber" : "testdoneraccessionnumber1",
      "donorInstituteCode" : "testdonorcode1"
    }, {
      "donorGermplasmPUI" : "testdonorid2",
      "donorAccessionNumber" : "testdoneraccessionnumber2",
      "donorInstituteCode" : "testdonorcode2"
    } ],
    "accessionNumber" : null,
    "commonCropName" : null,
    "speciesAuthority" : null,
    "germplasmName" : "test_germplasm_name",
    "germplasmPUI" : null,
    "instituteCode" : null
  }
}
```` 
+ **detail**: In this type of response, the "result" key contains only a data key, which is an arbitrarily long array of objects of the same type, as in GET /calls: 
````
{
  "metadata" : {
    "pagination" : {
      "totalCount" : 0,
      "pageSize" : 0,
      "totalPages" : 0,
      "currentPage" : 0
    },
    "status" : [ ],
    "datafiles" : [ ]
  },
  "result" : {
    "data" : [ {
      "call" : "calls",
      "methods" : [ "GET" ],
      "datatypes" : [ "JSON" ]
    }, {
      "call" : "studies-search",
      "methods" : [ "POST" ],
      "datatypes" : [ "JSON" ]
    }, {
      "call" : "germplasm/{id}",
      "methods" : [ "POST" ],
      "datatypes" : [ "JSON" ]
    }, {
      "call" : "studies/{id}/observationVariables",
      "methods" : [ "POST" ],
      "datatypes" : [ "JSON" ]
    }, {
      "call" : "allelematrices",
      "methods" : [ "GET" ],
      "datatypes" : [ "JSON" ]
    }, {
      "call" : "allelematrix-search",
      "methods" : [ "GET", "POST" ],
      "datatypes" : [ "FLAPJACK" ]
    } ]
  }
}
````

+ **master/detail**: This type of response, the "result" key contains both arbtirary properties and a "data" key, as in studies/{studyDbId}/observationVariables: 
````
{
  "metadata" : {
    "pagination" : {
      "totalCount" : 0,
      "pageSize" : 0,
      "totalPages" : 0,
      "currentPage" : 0
    },
    "status" : [ ],
    "datafiles" : [ ]
  },
  "result" : {
    "studyDbId" : 1,
    "trialName" : "trialname",
    "data" : [ {
      "scale" : {
        "scaleValidValues" : null,
        "scaleDbId" : "testid1",
        "name" : "testNameOne",
        "xref" : null,
        "datatype" : null,
        "decimalPlaces" : null
      },
      "status" : null,
      "ontologyName" : null,
      "ontologyDbId" : null,
      "contextOfUse" : null,
      "synonyms" : null,
      "scientist" : null,
      "date" : null,
      "crop" : null,
      "observationVariableDbId" : "testdbid1",
      "growthStage" : null,
      "name" : "testvariable1",
      "xref" : null,
      "method" : {
        "methodDbId" : "testdbid",
        "description" : null,
        "name" : "testmethodname",
        "reference" : null,
        "formula" : null,
        "class" : null
      },
      "language" : null,
      "defaultValue" : null,
      "trait" : {
        "traitDbId" : "testdbid",
        "status" : null,
        "description" : null,
        "entity" : null,
        "name" : "testtraitname",
        "xref" : null,
        "mainAbbreviation" : null,
        "attribute" : null,
        "synonyms" : null,
        "alternativeAbbreviations" : null,
        "class" : null
      },
      "institution" : null
    }, {
      "scale" : {
        "scaleValidValues" : null,
        "scaleDbId" : "testid2",
        "name" : "testNameOTwo",
        "xref" : null,
        "datatype" : null,
        "decimalPlaces" : null
      },
      "status" : null,
      "ontologyName" : null,
      "ontologyDbId" : null,
      "contextOfUse" : null,
      "synonyms" : null,
      "scientist" : null,
      "date" : null,
      "crop" : null,
      "observationVariableDbId" : "testdbid2",
      "growthStage" : null,
      "name" : "testvariable2",
      "xref" : null,
      "method" : {
        "methodDbId" : "testdbid2",
        "description" : null,
        "name" : "testmethodname2",
        "reference" : null,
        "formula" : null,
        "class" : null
      },
      "language" : null,
      "defaultValue" : null,
      "trait" : {
        "traitDbId" : "testdbid2",
        "status" : null,
        "description" : null,
        "entity" : null,
        "name" : "testtraitname2",
        "xref" : null,
        "mainAbbreviation" : null,
        "attribute" : null,
        "synonyms" : null,
        "alternativeAbbreviations" : null,
        "class" : null
      },
      "institution" : null
    } ]
  }
}
````

Additional documentation is in the [GitHub wiki](https://github.com/plantbreeding/documentation/wiki). 
See especially the [Best Practices and Conventions]
(https://github.com/plantbreeding/documentation/wiki/Best-Practices-and-Conventions).

### HTTP error codes

HTTP error codes are used as required, e.g., 200 for ok, 404 for page not found, 401 for not authorized, 501 for not implemented, 201 for created in a PUT, 202 for request received but not yet processed, etc.

All capturable errors should be responded to with the appropriate HTTP error code and a well forumlated JSON structure that includes a message describing the error.  The error code is intedended as a debugging tool for the service provider.  An example:

+ Response 400 (application/json) 

        { 
            "metadata" : {
                 "pagination": {
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [ {
                    "message": "Unable to parse POST request",
                    "code" : "" 
                } ],
                "datafiles": []
            },
            "result": {}
        }

### Asynchronous Processing

Some calls initiate asynchronous processing, which take an indeterminate amount of time to complete. For example, the allelematrix-search may initiate a background process that extracts the requested data from a data warehouse. In this case, 

* The status array of the call's response will contain a status object in which the value of the **code** key is **asynchid**, the value of the **message** key is an id that will be used in additional calls; 
* The resource from which the response was received will have a child resource called **status** to which the message value of the **asynchid** code is a uri parameter; a GET on this resource will indicate the current status of the job; 
* The status array of the response from the status resource will include a status object in which the key is called **asynchstatus** and the **message** key's value indicatse the following possible states with the specified meanings: 
        * PENDING: The background process has not started to work on the job; 
        * INPROCESS: The background process is working on the job;
        * FINISHED: The job has completed succesfully, in which case:
                * The datafiles list of the response with this **asynchstatus** message value is required to have at least one entry that is a file path or uri to the directory or file of interest; and/or
                * The data array in the result contains the matrix data;
        * FAILED: The job has failed;
* In the case where the message value of the **asynchstatus** code is FAILED, the status array may have, but is not requried to have, a status object in which the **code** key is **asynchfailure** and the **message** key indicates the cause of the job failure (some systems may prefer to use email notification either instead of or in addition to this mechanism). 

For example, a call to allelematrix-search might give the following response: 

<code>
{
    "metadata": {   
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [{"code": "asynchid", 
                     "message" : "extract_2016-12-15-20-37-015"}],
        "datafiles": []
    },
    "result" : { 
        "data": []
    }
}
</code>

Given this response, a GET on the resource **/allelematrix-search/status/extract_2016-12-15-20-37-015** will give a response as follows:

<code>
{
    "metadata": {   
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [{"code" : "asycnstatus" ,
                     "message" : "FINISHED"}],
        "datafiles": ["/shared_files/app_test/file_bundle/crops/rice/extract/output/721"]
    },
    "result" : { 
        "data": []
    }
}
</code>

### API call categories:  
Scope: "CORE", "PHENOTYPING", "GENOTYPING", "OTHER".  
Status: "STABLE", "ACCEPTED", "IN DISCUSSION", "SUGGESTED".
