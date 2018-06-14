
# Group Samples

API methods for tracking/managing plant samples and related meta-data. A 'Sample' in the context of BrAPI, is defined as the actual biological plant material collected from the field.




## Samples/{sampledbid} [Get /brapi/v1/samples/{sampleDbId}]

 Used to retrieve the details of a single Sample from a Sample Tracking system.
<a href="https://test-server.brapi.org/brapi/v1/samples"> test-server.brapi.org/brapi/v1/samples/{sampleDbId}</a> 

+ Parameters
    + sampleDbId (Required, string) ... the internal DB id for a sample


+ Response 200 (application/json)
```
{
    "result": {
        "sampleType": "TypeOfSample",
        "plateIndex": 0,
        "observationUnitDbId": "abc123",
        "germplasmDbId": "def456",
        "plateDbId": "PlateID-123",
        "tissueType": "TypeOfTissue",
        "plantDbId": "PlantID-123",
        "sampleTimestamp": "2016-07-27T14:43:22+01:00",
        "sampleDbId": "Unique-Plant-SampleID-1",
        "takenBy": "Mr. Technician",
        "notes": "Cut from infected leaf",
        "studyDbId": "StudyId-123",
        "plotDbId": "PlotId-123"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```

## Samples [Put /brapi/v1/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.
 

+ Parameters
 
+ Request (application/json)
/definitions/sample

+ Response 200 (application/json)
```
{
    "result": {
        "sampleDbId": "Unique-Plant-SampleID"
    },
    "metadata": null
}
```

## Samples-search [Post /brapi/v1/samples-search]

 Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.
<a href="https://test-server.brapi.org/brapi/v1/samples"> test-server.brapi.org/brapi/v1/samples-search</a> 

+ Parameters
 
+ Request (application/json)
/definitions/sampleSearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "sampleType": "TypeOfSample",
                "plateIndex": 0,
                "observationUnitDbId": "abc123",
                "germplasmDbId": "def456",
                "plateDbId": "PlateID-123",
                "tissueType": "TypeOfTissue",
                "plantDbId": "PlantID-123",
                "sampleTimestamp": "2016-07-27 13:43:22",
                "sampleDbId": "Unique-Plant-SampleID-1",
                "takenBy": "Mr. Technician",
                "notes": "Cut from infected leaf",
                "studyDbId": "StudyId-123",
                "plotDbId": "PlotId-123"
            },
            {
                "sampleType": "TypeOfSample",
                "plateIndex": 0,
                "observationUnitDbId": "a1b2c3",
                "germplasmDbId": "def456",
                "plateDbId": "PlateID-123",
                "tissueType": "TypeOfTissue",
                "plantDbId": "PlantID-123",
                "sampleTimestamp": "2016-07-27 13:43:22",
                "sampleDbId": "Unique-Plant-SampleID-2",
                "takenBy": "Mr. Technician",
                "notes": "Cut from infected leaf",
                "studyDbId": "StudyId-123",
                "plotDbId": "PlotId-123"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Samples-search [Get /brapi/v1/samples-search{?sampleDbId}{?observationUnitDbId}{?plateDbId}{?germplasmDbId}{?pageSize}{?page}]

 Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.
<a href="https://test-server.brapi.org/brapi/v1/samples"> test-server.brapi.org/brapi/v1/samples-search</a> 

+ Parameters
    + sampleDbId (Optional, string) ... the internal DB id for a sample
    + observationUnitDbId (Optional, string) ... the internal DB id for an observation unit where a sample was taken from
    + plateDbId (Optional, string) ... the internal DB id for a plate of samples
    + germplasmDbId (Optional, string) ... the internal DB id for a germplasm
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is 1000.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is 0.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "sampleType": "TypeOfSample",
                "plateIndex": 0,
                "observationUnitDbId": "abc123",
                "germplasmDbId": "def456",
                "plateDbId": "PlateID-123",
                "tissueType": "TypeOfTissue",
                "plantDbId": "PlantID-123",
                "sampleTimestamp": "2016-07-27 13:43:22",
                "sampleDbId": "Unique-Plant-SampleID-1",
                "takenBy": "Mr. Technician",
                "notes": "Cut from infected leaf",
                "studyDbId": "StudyId-123",
                "plotDbId": "PlotId-123"
            },
            {
                "sampleType": "TypeOfSample",
                "plateIndex": 0,
                "observationUnitDbId": "a1b2c3",
                "germplasmDbId": "def456",
                "plateDbId": "PlateID-123",
                "tissueType": "TypeOfTissue",
                "plantDbId": "PlantID-123",
                "sampleTimestamp": "2016-07-27 13:43:22",
                "sampleDbId": "Unique-Plant-SampleID-2",
                "takenBy": "Mr. Technician",
                "notes": "Cut from infected leaf",
                "studyDbId": "StudyId-123",
                "plotDbId": "PlotId-123"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```