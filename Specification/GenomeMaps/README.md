
# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome




## Maps [Get /brapi/v1/maps{?species}{?type}{?pageSize}{?page}]

Get list of maps <br>
<strong>Status:</strong> ACCEPTED <strong>Implemented by:</strong> Germinate, Cassavabase <strong>Used by:</strong> Flapjack do we need list of parents and specify mapping population? 

+ Parameters
    + species (Optional, string) ... Species name
    + type (Optional, string) ... Type of map
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "name": "Some Map",
                "publishedDate": "2008-04-16",
                "markerCount": 1000,
                "species": "Some species",
                "comments": "This map contains ...",
                "type": "Genetic",
                "unit": "cM",
                "mapDbId": "abc123",
                "linkageGroupCount": 7
            },
            {
                "name": "Some Other map",
                "publishedDate": "2009-01-12",
                "markerCount": 1501,
                "species": "Some Species",
                "comments": "this is blah blah",
                "type": "Genetic",
                "unit": "cM",
                "mapDbId": "def234",
                "linkageGroupCount": 7
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
        "status": [],
        "datafiles": []
    }
}
```

## Maps/{mapdbid} [Get /brapi/v1/maps/{mapDbId}{?pageSize}{?page}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup <br>
<strong>Status:</strong> ACCEPTED <strong>Implemented by:</strong> Germinate, Cassavabase <strong>Used by:</strong> Flapjack 

+ Parameters
    + mapDbId (Required, string) ... The internal db id of a selected map
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "name": "Some map",
        "unit": "cM",
        "mapDbId": "abc123",
        "data": [
            {
                "maxPosition": 10000000,
                "linkageGroupName": "1",
                "markerCount": 100000
            },
            {
                "maxPosition": 12347889,
                "linkageGroupName": "2",
                "markerCount": 1247
            }
        ],
        "linkageGroups": [
            "DEPRECATED - Replaced by 'data' in v1.1"
        ],
        "type": "Genetic"
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Maps/{mapdbid}/positions [Get /brapi/v1/maps/{mapDbId}/positions{?linkageGroupId}{?linkageGroupName}{?pageSize}{?page}]

markers ordered by linkageGroup and position <br>
<strong>Status:</strong> ACCEPTED. <strong>Implemented by:</strong> Germinate, Cassavabase <strong>Used by:</strong> Flapjack 

+ Parameters
    + mapDbId (Required, string) ... unique id of the map
    + linkageGroupId (Optional, string) ... <strong>Deprecated</strong> Use linkageGroupName instead
    + linkageGroupName (Optional, string) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "markerDbId": "1",
                "linkageGroupName": "1A",
                "markerName": "marker1",
                "location": "1000"
            },
            {
                "markerDbId": "2",
                "linkageGroupName": "1A",
                "markerName": "marker2",
                "location": "1001"
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
        "status": [],
        "datafiles": []
    }
}
```

## Maps/{mapdbid}/positions/{linkagegroupname} [Get /brapi/v1/maps/{mapDbId}/positions/{linkageGroupName}{?min}{?max}{?pageSize}{?page}]

markers ordered by linkageGroup and position 

+ Parameters
    + mapDbId (Required, string) ... unique id of the map
    + linkageGroupName (Required, string) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + min (Optional, integer) ... minimum position on linkage group
    + max (Optional, integer) ... maximum position on linkage group
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "markerDbId": "1",
                "markerName": "marker1",
                "location": "1000"
            },
            {
                "markerDbId": "2",
                "markerName": "marker2",
                "location": "1001"
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
        "status": [],
        "datafiles": []
    }
}
```