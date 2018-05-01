FORMAT: 1A

# BrAPI V1.3

The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. It is a <i>shared</i>, <i>open</i> API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. For more information, go to <a href="https://brapi.org/">brapi.org</a>.

### URL structure

API requests are structured as 

https://**_\<server\>_**/brapi/v1/**_\<call\>_**

where "v1" is the major version number of the API, followed by the desired REST `<call>`.
  
Example: _https://test-server.brapi.org/brapi/v1/markerprofiles/2939_ 

To distinguish between multiple databases available from the same server, include a base path as part of the `<server>` identifier. An arbitrary number of levels can be inserted between the domain name and the brapi level, if needed.

Example: _https://test-server.brapi.org/**maize\_db\_01**/brapi/v1/markerprofiles/2939_

Example: _https://test-server.brapi.org/**cornell/cals/wheat_db**/brapi/v1/markerprofiles/2939_

### Structure of the response object:

The return objects are encoded in JSON. The response consists of:
+ A "metadata" key containing pagination, status, and file information;
+ A "result" key that can contain:
  + Arbitrary properties; and/or
  + A "data" key containing an array of objects of the same type.


#### The Metadata Key

The metadata key is structured as followed:


````
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
           }
       ],
       "asynchStatus": {
           "asynchId": "abc123"
           "status": "PENDING",
           "startTime": "2017-06-16T14:47:23-0600",
           "endTime": null,
           "percentComplete": 0
       },
       "datafiles" : ["/mnt/local/matrix_01.csv",
                      "/mnt/local/matrix_02.csv"]
   }

````

+  **pagination**: The `pagination` object is applicable only when the payload contains a "data" key. It describes the pagination of the data contained in the "data" array, as a way to identify which subset of data is being returned. Pages are zero indexed, so the first page will be page 0 (zero).

+ **datafiles**: The `datafiles` key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.

+ **status**: The `status` object contains a list of objects with the keys "code" and "message". If no status is reported, an empty list should be returned. 

**NOTE:** The Status object should be used _in addition_ to the standard [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). The purpose is to provide additional, BrAPI specific information back to the client.   

The following are officially accepted status codes, though others maybe used for specific implementation needs.

Code|Message|Description
--|--|--
200|"Success"|Optional status for representing explicitly that the request was accepted and returned without any issue
2001|"Upload Successful"|New data was submitted to and accepted by the server
2002|"Async call in progress"|An Async call has been successfully started, See the section on Asynchronous Calls for more details.
400|"Failure"|Optional status for representing explicitly that the request was bad in some way
4001|"Could not update values for <object type>"| Error to be returned when the server is unable to store some data submitted
4002|"Missing required parameter <parameter name>"| Error to be returned when a required parameter is missing from request
4003|"Permission Denied"| Error to be returned when the user does not have permission to access the requested resource
4004|"No objects found for given parameters"| Error to be returned when there are no objects in the database which match the requested search parameters


+ **asynchStatus**: (Optional) The `asynchStatus` object is used to provide additional information around certain calls being performed asynchronously. See the section on Asynchronous Calls for more details.



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


### Error Handling

HTTP error codes are used as required, e.g., 200 for ok, 404 for page not found, 401 for not authorized, 501 for not implemented, 201 for created in a PUT, 202 for request received but not yet processed, etc.

All capturable errors should be responded to with the appropriate HTTP error code and a well formulated JSON structure that includes a message describing the error.  The error code is intended as a debugging tool for the service provider.

### Date and timestamp fields

Date and timestamp fields are coded in the ISO 8601 standard, extended format. If the field name ends in "Date", only the date portion should be provided, for example "2017-06-16". If a field ends in "Timestamp", the date, time and time zone information needs to be provided, as in this example: "2017-06-16T14:47:23-0600". In version 1, milliseconds are not supported.
--|Format|Example
--|--|--
Date|yyyy-MM-dd|2017-06-16
Timestamp|yyyy-MM-ddThh:mm:ssz|2017-06-16T14:47:23-0600
Timestamp UTC|yyyy-MM-ddThh:mm:ssZ|2017-06-16T20:47:23Z


### Location coordinate encoding

To encode locations as coordinates, the ISO 6709 standard is used, degree notation only. WGS84 is used as the geodetic datum spatial reference system.

||Unit|Format|Example|
|---|---|---|---|
|latitude|degrees|±DD.D|"+40.20361"|
|longitude|degrees|±DDD.D|"-075.00417"|
|altitude|meters|±M|"+127"|

Note:
 + Plus and minus signs are always required
 + Latitude has two digits before the decimal separator (with leading zeros when necessary)
 + Longitude has three digits before the decimal separator (with leading zeros when necessary)
 + Altitude is recorded in meters above the WGS84 reference ellipsoid (no leading zeros) 


### Search Services

There are several "Search" calls specified in BrAPI. These calls have a postfix of "-search" in the name, and are used to search for a set of entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a candidate key which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its fields. 

Each optional parameter included in any search service call should act as a filter on the data being returned. This means the search parameters should always have an 'AND' type relationship with each other. 

If NO parameters are used in the request, the search service should return ALL entities of the given type, since no filters are being applied. (Normal pagination defaults still apply)

Example: Given this data
```
{
    id: "1",
    first: "Bob",
    last: "Jones"
},{
    id: "2",
    first: "Bob",
    last: "Smith"
},{
    id: "3",
    first: "Alice",
    last: "Jones"
},{
    id: "4",
    first: "Cathy",
    last: "Jones"
}
```
The call `/person-search?first=Bob&last=Jones` will only return entity "1". The parameter `first` filters the data to just entities where the first name is "Bob" (entities "1" and "2"). The parameter `last` is an additional filter and further limits the data returned, resulting in just entity "1" satisfying both filters.

When parameters are defined as lists, each item in the list acts as an accepted value for that parameter. This can be thought of as an 'OR' relationship for items within the same list parameter, or it could be considered a 'value IN array' type operation by a database.

For example: Given the data above, the call `/person-search?first=Alice,Bob&last=Jones` will return entities "1" and "3". In this case, the parameter `first` filters the data to the first 3 entities, including all entities where the first name is 'Alice' OR 'Bob'. Again, the parameter `last` is an additional filter, further limiting the data returned, resulting in just  entities "1" and "3" satisfying both filters.

These rules for search parameters apply to both GET call query parameters and POST call body parameters.



### Asynchronous Processing

Some search calls initiate asynchronous processing, which take an indeterminate amount of time to complete.

Calls which could have asynchronous implementations:
+ GET /allelematrix-search
+ POST /allelematrix-search

If a search call has an asynchronous implementation, then the `asynchStatus` object in `metadata` must be populated. 
+ The `asynchId` (required) key will contain an id that will be used in additional polling status calls.  
+ The `status` (required) key will contain one of the following possible states with the specified meanings:
    + PENDING: The background process has not started to work on the job; 
    + INPROCESS: The background process is working on the job;
    + FINISHED: The job has completed successfully, in which case the `result` object will be populated with the requested data OR the `datafiles` array will have at least one data file URI which contains the requested data.
    + FAILED: The job has failed;
+ The `startTime` indicates the date and time when the call was first made.
+ The `endTime` indicates the date and time when the processing for the call is complete.
+ The `percentComplete` is an integer [range 0-100] which indicates how much of the process has completed. If a system has no way of detecting intermediate status, `percentComplete` may jump directly from 0 to 100 when processing is finished.

After making the initial asynch call and receiving an `asynchId`, all subsequent polling calls should go to `/asynch_call/{asynchId}` 

For example, a call to **`/allelematrix-search`** might give the following response: 

````
{
    "metadata": {   
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [{"code": "2002", 
                     "message" : "Asynchronous call in progress"}],
        "datafiles": [],
        "asynchStatus": {
           "asynchId": "abc123",
           "status": "PENDING",
           "startTime": "2017-06-16T14:47:23-0600",
           "endTime": null,
           "percentComplete": 0
        }
    },
    "result" : {}
}
````

Given this response, a GET on the resource **`/allelematrix-search/abc123`** will give a response as follows:

````
{
    "metadata": {   
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [{"code" : "200" ,
                     "message" : "FINISHED"}],
        "datafiles": ["https://example.org/shared_files/crops/rice/extract/output/721"],
        "asynchStatus": {
           "asynchId": "abc123",
           "status": "FINISHED",
           "startTime": "2017-06-16T14:47:23-0600",
           "endTime": "2017-06-16T14:49:65-0600",
           "percentComplete": 100
        }
    },
    "result" : {}
}
````

