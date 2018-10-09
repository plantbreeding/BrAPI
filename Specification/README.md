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
               "messageType" : "INFO",
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

+  **pagination**: The `pagination` object is applicable only when the payload contains a "data" key. It describes the pagination of the data contained in the "data" array, as a way to identify which subset of data is being returned. Pages are zero indexed, so the first page will be page 0 (zero). If the "data" key is not present in the results, pagination should be ignored. 

+ **datafiles**: The `datafiles` key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.

+ **status**: The `status` object contains a list of objects with the keys "message" and "messageType". The "messageType" contains a standard logging level (ie "INFO", "WARNING", etc), and the "message" is the log entry which accompanies the message type log level. If no status messages are reported, an empty list should be returned. 

**NOTE:** See the Error Handling documentation for some outlines on when it is appropriate to include and ERROR message in the status array. 

+ **asynchStatus**: (Optional) The `asynchStatus` object is used to provide additional information around certain calls being performed asynchronously. See the section on Asynchronous Calls for more details.

#### Payload

The BRAPI response payload, which is contained in the "result" key, allows for three different types of responses:
+ **master**: In this type of response, the "result" key consists of arbitrary properties without a "data" key (in this case, pagination does not apply). 
````
{
  "metadata" : {
    "pagination" : {},
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

Following the RESTful architecture standard, most errors in BrAPI should be reported back to the client using the appropriate HTTP status code. The status codes that BrAPI officially supports are outlined below. Any response which does NOT have a 200 status code should have a plain text body with a reasonable error message which can be displayed to a user if necessary. 

<table>
<tr>
<th style="text-align: left; vertical-align: top">Code</th>
<th style="text-align: left; vertical-align: top">Description</th>
<th style="text-align: left; vertical-align: top">Use Case</th>
</tr>

<tr style="vertical-align: top">
<td>200</td>
<td>OK</td>
<td>Use code 200 for every successful JSON response. The 'status' array in a response metadata may contain addition logged errors as described below.</td>
</tr>

<tr style="vertical-align: top">
<td>400</td>
<td>Bad Request</td>
<td>Use code 400 when there is something wrong with the request. This could be a problem with any of the query parameters or request body object. <br/>
 - Example: A malformed JSON object which does not match the expected schema <br/>
 - Example: A parameter is sent as a alphanumeric string but is expected to an integer</td>
</tr>

<tr style="vertical-align: top">
<td>401</td>
<td>Unauthorized</td>
<td>Use code 401 when the request does not pass authorization checks. This could be caused by a missing Authorization token header, if the token is expired, or can not be verified. 401 can be replaced by 403 if desired.</td>
</tr>

<tr style="vertical-align: top">
<td>403</td>
<td>Forbidden</td>
<td>Use code 403 when the user is not allowed to access the requested resource. This could be caused by a system level authorization error (as described by 401) or by a more granular user permission issue. </td>
</tr>

<tr style="vertical-align: top">
<td>404</td>
<td>Not Found</td>
<td>Most servers and libraries have automatic 404 errors built in for unknown paths tried against the server. Use 404 explicitly when there is a path parameter which can not be found. Most path parameters in BrAPI are DbIds of specific objects, so if a requested DbId doesn't exist in the database, return a 404. </td>
</tr>

<tr style="vertical-align: top">
<td>500</td>
<td>Internal Server Error</td>
<td>Status code 500 indicates that the server has malfunctioned in some way. Use 500 for all unexpected exceptions, code defects, or configuration issues. For security, it is a best practice to implement an explicit error handler which can hide the cause of the error from the client and return a generic error message. </td>
</tr>
</table>

##### When to use an ERROR in the 'status' array?

As of BrAPI v1.3, the 'status' array in the response metadata is reserved for sending additional logging messages from the server to the client. These status messages may contain "ERROR" logs, but they should not supersede HTTP status codes or be relied upon for critical error handling. For most errors, it is a best practice to use the appropriate HTTP status code. However, there are a few cases where it is acceptable to return an error message to a user via the "status" array in the return objects metadata. Generally, this is acceptable when the request is valid, but the server has determined the response is not what the user is intending. Another way to think about this is the difference between errors intended for a developer vs errors intended for an end user. HTTP status code errors should be primarily directed at developers building a tool, but status error log messages should be directed at the user of a system.

For example, making the request `GET /trials?locationDbId=abc123`. If there are no locations with the DbId of "abc123", then the server will not be able to find any trials which have that locationDbId. This is a valid request, and an empty "data" array is the correct response, but it would be nice to notify the user that they will never find any trials with this locationDbId. 

Another example, making the request `GET /studies?studyType=Genotyping`. If the database does not contain any information about study types, then it is important to notify the user that the study type query parameter will be ignored. 


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

After making the initial asynch call and receiving an `asynchId`, all subsequent polling calls should go to `/{asynch_call}/{asynchId}` 

For example, a call to **`POST /allelematrix-search`** might give the following response: 

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

Given this response, polling the resource **`GET /allelematrix-search/abc123`** will give a response as follows:

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