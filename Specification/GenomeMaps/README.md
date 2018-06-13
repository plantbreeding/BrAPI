
# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome




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
        "data": [
            {
                "markerCount": 100000,
                "linkageGroupName": "1",
                "maxPosition": 10000000
            },
            {
                "markerCount": 1247,
                "linkageGroupName": "2",
                "maxPosition": 12347889
            }
        ],
        "linkageGroups": [
            "DEPRECATED - Replaced by 'data' in v1.1"
        ],
        "mapDbId": "abc123",
        "type": "Genetic"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "markerName": "marker1",
                "location": "1000",
                "markerDbId": "1"
            },
            {
                "markerName": "marker2",
                "location": "1001",
                "markerDbId": "2"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "markerName": "marker1",
                "linkageGroupName": "1A",
                "location": "1000",
                "markerDbId": "1"
            },
            {
                "markerName": "marker2",
                "linkageGroupName": "1A",
                "location": "1001",
                "markerDbId": "2"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

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
                "unit": "cM",
                "publishedDate": "2008-04-16",
                "species": "Some species",
                "name": "Some Map",
                "linkageGroupCount": 7,
                "markerCount": 1000,
                "mapDbId": "abc123",
                "comments": "This map contains ...",
                "type": "Genetic"
            },
            {
                "unit": "cM",
                "publishedDate": "2009-01-12",
                "species": "Some Species",
                "name": "Some Other map",
                "linkageGroupCount": 7,
                "markerCount": 1501,
                "mapDbId": "def234",
                "comments": "this is blah blah",
                "type": "Genetic"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```