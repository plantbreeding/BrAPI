FORMAT: 1A

# BrAPI V1.1

The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. It is a <i>shared</i>, <i>open</i> API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. For more information, go to <a href="https://brapi.org/">brapi.org</a>.

### URL structure

API requests are structured as "\<server\>/brapi/v1/", where "v1" is the major version number of the API, followed by the command.
  
Example: test.brapi.org/brapi/v1/markerprofiles/2939 

To distinguish between multiple databases or crops available from the same server, include the database or crop name as part of the "\<server\>" identifier. An arbitrary number of levels can be inserted between the domain name and the crops or brapi level, if needed.

Example: test.brapi.org/maize/brapi/v1/markerprofiles/2939

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
            "totalCount" : 1234,
            // total number of elements available in the super set (unpaged)
            "pageSize" : 200,
            // number of elements in the current returned page
            "totalPages" : 7,
            // total number of pages available (total count / requested page size)
            "currentPage" : 2
            // index number of the current returned page
       },
       "status" : [
           {
               "code" : "200",
               "message" : "Success"
           },{
               "code" : "asynchstatus",
               "message" : "PENDING"
           }
           ],
       "datafiles" : ["/mnt/local/matrix_01.csv",
                      "/mnt/local/matrix_02.csv"]
       }, . . . 
}

````

+  **pagination**: The pagination object is applicable only when the payload contains a "data" key. It describes the pagination of the data contained in the "data" array, as a way to identify which subset of data is being returned. Pages are zero indexed, so the first page will be page 0 (zero).

+ **datafiles**: The datafiles key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.

+ **status**: The status object contains a list of objects with the keys "code" and "message". If no status is reported, an empty list should be returned. The following are officially accepted status codes:

Code|Message|Description
--|--|--
asynchid|<arbitrary ID String>|Used for the first part of an asynchornous call, returns an ID string which can be used in a subsequent call to retrieve data or status information.
asynchstatus|"PENDING"|Indicates an asynchornous call is still working and will not return data yet.
asynchstatus|"FINISHED"|Indicates an asynchornous call is finished and this response object contains the requested data.
200|"Success"|Optional status for representing explicitly that the request was accepted and returned without any issue
40|"No objects found for given parameters"| Error to be returned when there are no objects in the database which match the requested search parameters
41|"Missing required parameter <parameter name>"| Error to be returned when a required parameter is missing from request
42|"Could not update values for <object type>"| Error to be returned when the server is unable to store some data submitted

#### Payload

The BRAPI response payload, which is contained in the "result" key, allows for three different types of responses:
+ **master**: In this type of response, the "result" key consists of arbitrary properties without a "data" key (in this case, pagination does not apply). 
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
	"key0": "master",
	"key1": 20,
	"key2": [ "foo", "bar", "baz" ]
  }
}
```` 
+ **detail**: In this type of response, the "result" element only contains the "data" key, which is an arbitrarily long array of objects of the same type. 
````
{
  "metadata" : {
    "pagination" : {
      "totalCount" : 20,
      "pageSize" : 3,
      "totalPages" : 7,
      "currentPage" : 0
    },
    "status" : [ ],
    "datafiles" : [ ]
  },
  "result" : {
    "data" : [ 
      {
        "detailKey0" : "detail0",
        "detailKey1" : [ "foo", "bar" ]
      }, 
      {
        "detailKey0" : "detail1",
        "detailKey1" : [ "bar", "baz" ]
      }, 
      {
        "detailKey0" : "detail2",
        "detailKey1" : [ "baz", "foo" ]
      },
    ]
  }
}
````

+ **master/detail**: In this type of response, the "result" key contains both arbtirary properties and the "data" key. 
````
{
  "metadata" : {
    "pagination" : {
      "totalCount" : 20,
      "pageSize" : 3,
      "totalPages" : 7,
      "currentPage" : 0
    },
    "status" : [ ],
    "datafiles" : [ ]
  },
"result" : {
	"key0": "master",
	"key1": 20,
	"key2": [ "foo", "bar", "baz" ],
    "data" : [ 
      {
        "detailKey0" : "detail0",
        "detailKey1" : [ "foo", "bar" ]
      }, 
      {
        "detailKey0" : "detail1",
        "detailKey1" : [ "bar", "baz" ]
      }, 
      {
        "detailKey0" : "detail2",
        "detailKey1" : [ "baz", "foo" ]
      },
    ]
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

### Date and timestamp fields

Date and timestamp fields are coded in the ISO 8601 standard, extended format. If the field name ends in "Date", only the date portion should be provided, for example "2017-06-16". If a field ends in "Timestamp", the date, time and time zone information needs to be provided, as in this example: "2017-06-16T14:47:23-0600". In version 1, milliseconds are not supported.
--|Format|Example
--|--|--
Date|yyyy-MM-dd|2017-06-16
Timestamp|yyyy-MM-ddThh:mm:ssz|2017-06-16T14:47:23-0600
Timestamp UTC|yyyy-MM-ddThh:mm:ssZ|2017-06-16T20:47:23Z

### Location coordinate encoding

To encode locations as coordinates, the ISO 6709 standard is used. Importantly, the decimal notation is used. Example
latitude: +40.20361, longitude: -075.00417. Note that plus and minus signs are always required, and latitude has two digits before the decimal separator (with leading zeroes when necessary), and longitude has three digits.

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
