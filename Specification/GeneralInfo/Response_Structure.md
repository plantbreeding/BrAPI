
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
    The `pagination` object is applicable only when the result payload contains the "data" key. It describes the pagination of the records contained in the "data" array, as a way to identify which subset of data is being returned.  

    If the "data" key is not present in the results, pagination should be ignored. All of the following responses are acceptable, and should be ignored equally.
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


#### Payload

The BRAPI response payload, which is contained in the "result" key, allows for three different types of responses:
+ **Single Response**: In this type of response, the "result" key consists of arbitrary properties without a "data" key (in this case, pagination does not apply). 
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
+ **List Response**: In this type of response, the "result" element only contains the "data" key, which is an arbitrarily long array of objects of the same type. 
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

Additional documentation is in the [BrAPI Wiki](https://wiki.brapi.org/index.php/BrAPI). 
See especially the [Best Practices](https://wiki.brapi.org/index.php/Best_Practices).
