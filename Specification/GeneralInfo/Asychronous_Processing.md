

### Asynchronous Processing

Some calls initiate asynchronous processing, which take an indeterminate amount of time to complete. For example, the allelematrix-search may initiate a background process that extracts the requested data from a data warehouse. In this case, 

+ The status array of the call's response will contain a status object in which the value of the **code** key is **asynchid**, the value of the **message** key is an id that will be used in additional calls; 
+ The resource from which the response was received will have a child resource called **status** to which the message value of the **asynchid** code is a uri parameter; a GET on this resource will indicate the current status of the job; 
+ The status array of the response from the status resource will include a status object in which the key is called **asynchstatus** and the **message** key's value indicatse the following possible states with the specified meanings:
    + PENDING: The background process has not started to work on the job; 
    + INPROCESS: The background process is working on the job;
    + FINISHED: The job has completed succesfully, in which case:
        + The datafiles list of the response with this **asynchstatus** message value is required to have at least one entry that is a file path or uri to the directory or file of interest; and/or
        + The data array in the result contains the matrix data;
    + FAILED: The job has failed;
+ In the case where the message value of the **asynchstatus** code is FAILED, the status array may have, but is not requried to have, a status object in which the **code** key is **asynchfailure** and the **message** key indicates the cause of the job failure (some systems may prefer to use email notification either instead of or in addition to this mechanism). 

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
