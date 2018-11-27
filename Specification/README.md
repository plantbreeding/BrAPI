FORMAT: 1A

# BrAPI V1.3

The Breeding API (BrAPI) is an interface for exchanging plant phenotype and genotype data between crop breeding applications. BrAPI is a standardized specification, meaning that any application may create their own implementation and that all of those implementations should be compatible. It is a <i>shared</i>, <i>open</i> API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. For more information, go to <a href="https://brapi.org/">brapi.org</a>.

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

    **NOTE:** When the `data` key is not present and no pagination is required, all of the following are acceptable, and should be ignored equally.
      - No `pagination` key in the meta data
      - "pagination": null
      - "pagination": {}
      - "pagination": {"totalCount" : 0, "pageSize" : 0, "totalPages" : 0, "currentPage" : 0}

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

-- | Format | Example
--|--|--
Date | yyyy-MM-dd | 2017-06-16
Timestamp | yyyy-MM-ddThh:mm:ssz | 2017-06-16T14:47:23-0600
Timestamp UTC | yyyy-MM-ddThh:mm:ssZ | 2017-06-16T20:47:23Z


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
 

#### Image Locations with GeoJSON

The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 

### Search Services

---
** NOTE ** : There have been significant changes to the structure of the Search Service calls in BrAPI v1.3. If you are looking for the v1.2 Search Service documentation please look <a href="https://github.com/plantbreeding/API/blob/V1.2/Specification/GeneralInfo/Search_Services.md">HERE</a>.

---

** NOTE **: Throughout this article, the word "entity" is used as a general term to describe a number of BrAPI objects which have search services available. This includes "germplasm", "images", "markers", "observationtables", "observationunits", "programs", "samples", "studies", and "variables"

---

There are several "Search" calls specified in BrAPI. The calls all start with `/search/...`, and are used to search for entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a candidate key, which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its fields. 

### Changes from v1.2

Most Search service calls in BrAPI v1.2 had two calls with the following structures:

```
    GET /entity-search?param=value...
      Returns -> A list of "entities" filtered by the parameters
    
    POST /entity-search
      Body -> {"param": ["value1", "value2"...]}
      Returns -> A list of "entities" filtered by the parameters
```

In BrAPI v1.3 we have shifted to a more RESTful paradigm. 

The original v1.2 `GET` call has simply removed the `-search` postfix, so the client is getting a filtered list of entities based on query parameters. The new call should work the same as its predecessor.

The original v1.2 `POST` call has been split into two calls: a `POST` for submitting a new search request object, and a `GET` for retrieving the results of that search.

```
    GET /entity?param=value...
      Returns -> A list of "entities" filtered by the parameters
    
    POST /search/entity
      Body -> {"param": ["value1", "value2"...]}
      Returns -> A search results DbId to be used to retrieve the results
    
    GET /search/entity/{searchResultsDbId}
      Returns -> A list of "entities" filtered by the parameters in the related POST call
```

#### Rational

There have been many questions about why we chose to move to a more complex searching structure. The new `/search` calls do increase the complexity of implementation, but they also improve the flexibility of implementation. By separating the search request and the response data, the server has some control over when and how often a database query is run. By providing a persistent search results DbId, it becomes possible for a client to make a single search request, then repeatedly reference the same results URL as many times as needed. This new paradigm will also open the door to much more complex query requests in future iterations of BrAPI. 

Below are descriptions of two possible implementation paths. The first is the simplest and is meant to act the most like the original, the second is a more complex implementation but more fully allows for the advantages described above. 


### v1.3 Implementation Options

#### Option #1: Store the Request

In this implementation, you will need to create a new table in your database, which can hold the search parameters submitted by the `POST` call. The exact structure of this table depends on your database technology and your organizations best practices for databases. In this table, you need to record a unique ID for each search, what type of search it is, and the parameters of the search request. Below is an example table that could do the job, though it is simplified for the purposes of this example. Always consider proper normalization and indexing techniques when building a new table. 

```
    search_request_id   | search_request_type    | parameter_name   | parameter_value 
    --------------------+------------------------+------------------|------------------------
    a1b2c3              | germplasm              | germplasmDbIds   | GERM01, GERM02, GERM03
    a1b2c3              | germplasm              | germplasmNames   | Germ 01, Germ 02
    b2c3d4              | studies                | programNames     | Program_1, Program_2
    b2c3d4              | studies                | germplasmDbIds   | GERM01
```

With each new search request stored, the unique search id (`search_request_id` from above) can be returned to the client as the `searchResultsDbId`. When the client makes a subsequent `GET` request, all the information about the search parameters can be collected from this table and the appropriate query can be generated. This means you are running a potentially slow query during the `GET` request, and it will be re-run on every subsequent `GET` request to the same ID. This is the most similar to the v1.2 version of the search service. 

```
Pros: Easy to implement, Most similar to the previous behavior, smallest data foot print
Cons: A potentially expensive search query must be run on the database for every GET request

Fits best with a "Search once, retrieve once" client expectation
```

#### Option #2: Store the Results

In this implementation, you will need two new tables, one to store some request data (as in Option #1), and one to store the results of each search. You will be consuming the search parameters immediately during the `POST` call, so it is not necessary to store all the parameter data, but it might be useful for audit purposes. The second table for storing results will be a join table between the search request and the primary entity being searched for. For example, if you are implementing the search for Germplasm, the table might look something like the table below. You might decide to create one table per search type, or group all your search results records into one table for all search types. 

```
    search_request_id   | germplasm_id    
    --------------------+-----------------
    a1b2c3              | GERM010590
    a1b2c3              | GERM010571
    a1b2c3              | GERM010542
    a1b2c3              | GERM010402
    b2c3d4              | GERM010542
    b2c3d4              | GERM010402
```

A word of caution in this implementation: recording the results of every search has the potential to make very large tables. The purpose of this design is to cache the results of a query and make subsequent search requests faster. If the search query you are using is already fast enough, this solution might not be right for you. Another option to think about is putting an expire time on each set of search results, and an automatic process for removing expired results. This can make the service a much more complicated to implement but it means you do not have to maintain all search results forever. Make sure your implementation is well documented so clients and other developers are not surprised if the search results they had cached yesterday are gone today.

```
Pros: Provides cached result for quick retrieval, the search results will be maintained statically
Cons: More complicated to implement and maintain

Fits best with a "Search once, retrieve many times" client expectation
```

### General Implementation Notes

#### GET Entity

The entity filter services (previously the `GET /entity-search` services) have the form `GET /entity?param=value`. Each optional parameter these services should act as a filter on the data being returned. This means the filter parameters should always have an 'AND' type relationship with the others. If NO parameters are used in the request, the service should return ALL entities of the given type, since no filters are being applied (Normal pagination defaults still apply). If one parameter is used, the service should return the entities that match the parameter. If two parameters are used, the service should return the entities that match both parameters. 

Example: Given the entity "Names" and this data ("Names" is a fake entity for simple example purposes only) 

```
    id   | first   | last
    -----+---------+--------
    "01" | "Bob"   | "Jones"
    "02" | "Bob"   | "Smith"
    "03" | "Alice" | "Jones"
    "04" | "Cathy" | "Evans"
```

The request `GET /names`, with no parameters, will return ALL of the names available in the database.

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
        last: "Evans"
    }
```

The request `GET /names?first=Bob` will return all the records where the `first` field equals "Bob". In this case, there are two records.

```
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    },{
        id: "2",
        first: "Bob",
        last: "Smith"
    }
```

The request `GET /names?first=Bob&last=Smith` will return all the records where the `first` field equals "Bob" AND where the `last` field equals "Smith". Only one record matches those criteria.

```
    {
        id: "2",
        first: "Bob",
        last: "Smith"
    }
```

The request `GET /names?first=Bob&last=Evans` will return no records because there are no records where the `first` field equals "Bob" AND where the `last` field equals "Evans". 


#### POST Search, GET Results

As of BrAPI v1.3, searching for entities using the POST method has been split into two calls. The first call `POST /search/entity` submits a new search request to the server and returns an ID unique to that search instance. The second call `GET /search/entity/{searchResultsDbId}` returns the results of that search. Each POST call has a different Body object specification with search parameters specific to the given entity. The GET call has pagination parameters available so the client can limit the amount of data they get back for a given search. 

Most parameters in the POST Body object are arrays of strings. The array should be populated with all the search terms the client wishes to filter on, so each element in the array should have an "OR" relationship with the others. For example, using the data above, the search request object `{"first":["Alice", "Cathy", "Dave"]}` should return the records where `first` equals "Alice" OR "Cathy" OR "Dave". "Dave" has no record in our data, but records for "Alice" and "Cathy" will be returned. This can also be considered a 'WHERE value IN array' type operation by a database.

```
POST /search/names
    {
        "first":["Alice", "Cathy", "Dave"]
    }

GET /search/names/a1b2c3
    {
        id: "3",
        first: "Alice",
        last: "Jones"
    },{
        id: "4",
        first: "Cathy",
        last: "Evans"
    }
```

As above, when multiple parameters are used together, they have an "AND" relationship. For example, search request object `{"first":["Bob"], "last": ["Jones"]}` will return the records where `first` equals "Bob" AND `last` equals "Jones". There is only one record in our data set which matches this criteria.

```
POST /search/names
    {
        "first":["Bob"], 
        "last": ["Jones"]
    }

GET /search/names/b2c3d4
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    }
```

Combining these ideas, each array parameter should be resolved independently, then "ANDed" together. For example, search request object `{"first":["Alice", "Bob", "Cathy"], "last": ["Jones"]}` will return the records where (`first` equals "Alice" OR "Bob" OR "Cathy") AND (`last` equals "Jones"). This criteria matches "Alice Jones" and "Bob Jones" but it does not match "Cathy Evans". 

```
POST /search/names
    {
        "first":["Alice", "Bob", "Cathy"], 
        "last": ["Jones"]
    }

GET /search/names/c3d4e5
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    },{
        id: "3",
        first: "Alice",
        last: "Jones"
    }
```

Some searchable entities have non-array parameters in their request body objects. These are generally for things like numbers and dates where a client might be interested in a certain range instead of an exact value. Numeric fields with the suffix "Min" or "Max" describe the minimum and maximum values to search for (inclusive). Date string fields with the suffix "Start" or "End" should be treated as the beginning and ending (respectively) of a time range (inclusive).





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
