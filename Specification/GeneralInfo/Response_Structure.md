
### Structure of the response object:

The return objects are encoded in JSON. A normal response consists of:
+ An optional `@context` field used for defining fields used by JSON-LD
+ A required `metadata` field containing pagination info, status logging messages, and extra linked file information
+ A required `result` field that contains the payload of requested data. Depending on what request was made, this payload might be a single object or an array of objects

#### @Context

The `@context` field is used for defining fields used by JSON-LD. `@context` should be an array of URLs which point to JSON-LD context files. `@context` is optional and should only be included in a response if the requesting client uses JSON-LD. More information on JSON-LD can be found at [json-ld.org](https://json-ld.org/).

#### Metadata

The `metadata` field should have the following structure:


````
"metadata" : {
  "pagination" : {
    "totalCount" : 1234,
    "pageSize" : 200,
    "totalPages" : 7,
    "currentPage" : 2
  },
  "status" : [
    {
      "messageType" : "INFO",
      "message" : "Success"
    }
  ],
  "datafiles": [
    {
      "fileDescription": "This is an Excel data file",
      "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
      "fileName": "datafile.xlsx",
      "fileSize": 4398,
      "fileType": "application/vnd.ms-excel",
      "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
    }
  ]
}

````

+  **pagination**: 
    The `pagination` object is applicable only when the `result` payload contains a `data` field. It describes the pagination of the records contained in the `data` array, as a way to identify which subset of data is being returned.  

    If the `data` key is not present in the results, pagination should be ignored. All of the following responses are acceptable, and should be ignored equally.
      - `pagination` key omitted from the metadata
      - `"pagination": null`
      - `"pagination": {}`
      - `"pagination": {"totalCount" : 0, "pageSize" : 0, "totalPages" : 0, "currentPage" : 0}`
      
    Most endpoints in BrAPI use page index numbers to determine how to get the next page of data. Page numbers start at zero, so the first page will be page 0 (zero). When appropriate, a request will have two parameters for paging: `page` and `pageSize`. `page` allows the client to request a specific page number. Page numbers start at zero, so the first page will be `?page=0`. `pageSize` allows the client to control the maximum number of records that will be returned per page. A typical paged response will have four fields: `currentPage`, `pageSize`, `totalCount` and `totalPages`. `currentPage` is the number for the current returned page. In most cases, this will be a confirmation of the requested `page` parameter. If `page` is not populated in the request, then `currentPage` should have the default value zero, indicating the first page of data was retrieved by default. `pageSize` indicates the number of records in the current response page. `totalCount` indicates the total number of records available in the unpaged super set. `totalPages` indicates the total number of pages available and can be calculated with the formula `totalCount` / `requested pageSize`. 
    
    **Note:** A small subset of BrAPI endpoints use a `nextPageToken` instead of an page number. These endpoints are related to Genotyping and the alternative paging scheme is better suited to handle larger data sets. These endpoints are clearly marked as different from the norm and the paging mechanism is described in more detail in the endpoint descriptions.     

+ **status**: 
    The `status` array contains a list of important logging messages that the server wants to pass to the client. This could include things like information about successful data upload, warnings about ignored parameters, or errors about minor data validations. Each status object has two keys: "message" and "messageType". The "messageType" contains a standard logging level (ie "INFO", "WARNING", etc), and the "message" is the log text. If no status messages are reported, an empty list should be returned. 

    **NOTE:** See the Error Handling documentation for some outlines on when it is appropriate to include and ERROR message in the status array. 

+ **datafiles**: 
    The `datafiles` array contains a list of generic file description. These files contain additional information related to the returned object and can be retrieved by a subsequent call to the `fileURL` provided. `fileURL` should be a full URL pointing to the files location. `fileName` is the name of the file, `fileDescription` is the text description of the file, `fileSize` is the size of the file in bytes, and `fileType` is the full MIME type for the file. `fileMD5Hash` contains a string which is the result of running the MD5 Hashing algorithm on the file and this can be used as a check sum to confirm that the file was downloaded correctly. 


#### Result

The `result` field contains the payload of requested data. Depending on what request was made, this payload might be a **Single Response** or a **List Response**

+ **Single Response**: In this type of response, the `result` field is an object describing a single record of data. There should NOT be a `data` array in this case and pagination does not apply. A **Single Response** is used when you are requesting or modifying a single, specific data object by its DbId. 
````
{
  "metadata" : {
    "pagination" : {},
    "status" : [ ],
    "datafiles" : [ ]
  },
  "result" : {
    "key0": "name1",
    "key1": 20,
    "key2": [ "foo", "bar", "baz" ]
  }
}
```` 
+ **List Response**: In this type of response, the `result` object only contains a `data` field, which is an arbitrarily long array of objects of the same type. Pagination request parameters and pagination metadata fields apply to this `data` array. 
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
	    "key0": "name1",
	    "key1": 20,
	    "key2": [ "foo", "bar", "baz" ]
      }, 
      {
	    "key0": "name2",
	    "key1": 21,
	    "key2": [ "sin", "cos", "tan" ]
      }, 
      {
	    "key0": "name3",
	    "key1": 22,
	    "key2": [ "grumpy", "sleepy", "dopey" ]
      },
    ]
  }
}
````

#### Special Cases

There are a small number BrAPI endpoints which have exceptions to these general rules. Please review the response schema carefully when you are working with any of the following.

+ **Lists** The endpoint `/lists/{listDbId}` should return an object that with all the fields to describe a single list AND a `data` array with the contents of the list. Since a List object could have any number of items in it, it is important that the client can control the pagination of the list contents and pagination only applies to the `data` array. 
+ **Calls** There are few different endpoints which end with `.../calls` and they all return a list of Allele Call objects. The genotype text string for the Calls can be formated differently with different separator and unknown value characters. So all `.../calls` endpoints should respond with a `data` array with the Call objects AND a set of fields which describe the formatting of all the Call objects in the array.
+ **Tables** The endpoints `/observation/table` and `/observationunits/table` can both produce a table structure of data. The `Accept` header is used as input to producedifferent possible formats including CSV, TSV, and JSON. Selecting CSV and TSV should return table data as text using the appropriate separators. JSON should return an object with fields defining a the header row of the table, as well as the `data` array. Each item in the `data` array is a row in the table and is represented as an array of strings. This means Pagination can be applied to the rows of data, but not the columns. 
+ **Errors** Error responses with status codes in the 400's and 500's should not follow the standard response pattern. Checkout the documentation on [Error Handling](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Error_Handling.md) for more info. 


Additional documentation is in the [BrAPI Wiki](https://wiki.brapi.org/index.php/BrAPI). 
See especially the [Best Practices](https://wiki.brapi.org/index.php/Best_Practices).
