

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
