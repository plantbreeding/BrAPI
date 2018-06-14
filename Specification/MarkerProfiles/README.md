
# Group Markerprofiles

For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*

Basic concepts in the **Breeding API**:

- *markerprofile*: A set of marker scores for a specific extract from a specific germplasm.
- *extract* : a preparation from a germplasm for an analysis. 
- *sample*: an individual plant or tissue from a plant of a particular germplasm
- *germplasm*: a single genetic entity (cultivar, variety, accession, breeding line) used for analysis
- *marker*: a DNA sequence polymorphism, potentially localized to a single genomic location
- *allele*: one of the two possible states of a marker in each haploid chromosome complement of a specified germplasm, as determined in a specified experiment. A diploid organism has two alleles per marker.
- *missing*: a germplasm/marker/experiment combination for which no allele result is available, whether it was tested for or not




## Allelematrix-search [Get /brapi/v1/allelematrix-search{?markerprofileDbId}{?markerDbId}{?matrixDbId}{?format}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageSize}{?page}]

Status: ACCEPTED.

Implemented by: Germinate (POST only), Cassavabase

Used by: Flapjack (POST only)

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

See Search Services for additional implementation details.
</br>
This uses a more efficient data structure and pagination for large number of markers. 
</br>
Use GET when parameter size is less than 2K bytes.
This method may support asynchronous processing. 

+ Parameters
    + markerprofileDbId (Optional, array) ... The markerprofile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
    + markerDbId (Optional, array) ... ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerprofileDbId' or 'matrixDbId' is present.
    + matrixDbId (Optional, array) ... 
    + format (Optional, string) ... format for the datafile to be downloaded. tsv and csv currently supported; flapjack may be supported.
    + expandHomozygotes (Optional, boolean) ... Should homozygotes NOT be collapsed into a single occurrence?
    + unknownString (Optional, string) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (Optional, string) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (Optional, string) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```

## Allelematrix-search [Post /brapi/v1/allelematrix-search]

Status: ACCEPTED.

Implemented by: Germinate (POST only), Cassavabase

Used by: Flapjack (POST only)

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

Use POST when parameter size is greater than 2K bytes.

- If no format is specified, this call returns the data in JSON form.

- If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the "datafiles" field of the "metadata".

- If more than one format is requested at a time, the server will throw a "501 Not Implemented" error.

The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats) 

+ Parameters
 
+ Request (application/json)
/definitions/alleleMatrixSearchRequest

+ Response 200 (application/tsv)
```
{
    "result": {
        "data": []
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": [
            "https://my-fancy-server/files/allelematrix-1234.tsv"
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Markerprofiles/{markerprofiledbid} [Get /brapi/v1/markerprofiles/{markerprofileDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageSize}{?page}]

<strong>Scope</strong>:GENOTYPING.
<strong>Status</strong>: ACCEPTED.
<strong>Implemented by</strong>: Germinate, Cassavabase
</br>
For the requested markerprofile ID, returns the allele call for each marker. 
[Example](http://malt.pw.usda.gov/t3/wheatplus/markerprofiles/1784_99/count?analysisMethod=GoldenGate)
</br>
<strong>Allele encodings</strong>

- Unknown data will by default be encoded by "N"
- Homozygotes are returned as a single occurance, e.g. AA -> A, GG -> G
- Phased heterozygotes are by default separated by a pipe ("|") and unphased heterozygotes are by default separated by a forward slash ("/")
- Dominant markers such as DArTs: 1 for present, 0 for absent

<strong>Parameters</strong>
- If the user would like to use an empty string ("") for any of the parameters, the value should be set to the reserved word "empty_string", e.g. sepUnphased=empty_string.

<strong>Open issue:</strong>
The pages of data will need to be sorted sensibly in order for the
requested page to be delivered consistently.  By map or genome position?
Alphabetically?' 

+ Parameters
    + markerprofileDbId (Required, string) ... The server's internal id for the markerprofile
    + expandHomozygotes (Optional, boolean) ... Should homozygotes NOT be collapsed into a single orrucance?
    + unknownString (Optional, string) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (Optional, string) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (Optional, string) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
    + pageSize (Optional, integer) ... The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    + page (Optional, integer) ... Required if `pageSize` is given; and requires that `pageSize` be given. The page indexing starts at 0 (the first page is 'page'=0)


+ Response 200 (application/json)
```
{
    "result": {
        "uniqueDisplayName": "My Fancy Germplasm",
        "markerprofileDbId": "993",
        "germplasmDbId": "1",
        "analysisMethod": "GBS",
        "data": [
            {
                "marker1-1": "1"
            },
            {
                "marker1-2": "0"
            },
            {
                "marker1-3": "0"
            },
            {
                "marker1-4": "0"
            },
            {
                "marker1-5": "0"
            },
            {
                "marker1-6": "1"
            },
            {
                "marker1-7": "0"
            },
            {
                "marker1-8": "0"
            },
            {
                "marker1-9": "0"
            },
            {
                "marker1-10": "1"
            },
            {
                "marker1-11": "0"
            },
            {
                "marker2-1": "0"
            },
            {
                "marker2-2": "1"
            },
            {
                "marker2-3": "1"
            },
            {
                "marker2-4": "1"
            },
            {
                "marker2-5": "0"
            },
            {
                "marker3-1": "1"
            },
            {
                "marker3-2": "1"
            },
            {
                "marker3-3": "0"
            },
            {
                "marker3-4": "0"
            },
            {
                "marker3-5": "0"
            },
            {
                "marker3-6": "0"
            }
        ],
        "extractDbId": "extract1"
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 22,
            "pageSize": 22,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```

## Allelematrices-search [Get /brapi/v1/allelematrices-search{?markerprofileDbId}{?markerDbId}{?matrixDbId}{?format}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageSize}{?page}]

Status: ACCEPTED.

Implemented by: Germinate (POST only), Cassavabase

Used by: Flapjack (POST only)

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

See Search Services for additional implementation details.
</br>
This uses a more efficient data structure and pagination for large number of markers. 
</br>
Use GET when parameter size is less than 2K bytes.
This method may support asynchronous processing. 

+ Parameters
    + markerprofileDbId (Optional, array) ... The markerprofile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
    + markerDbId (Optional, array) ... ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerprofileDbId' or 'matrixDbId' is present.
    + matrixDbId (Optional, array) ... 
    + format (Optional, string) ... format for the datafile to be downloaded. tsv and csv currently supported; flapjack may be supported.
    + expandHomozygotes (Optional, boolean) ... Should homozygotes NOT be collapsed into a single occurrence?
    + unknownString (Optional, string) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (Optional, string) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (Optional, string) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```

## Allelematrices-search [Post /brapi/v1/allelematrices-search]

Status: ACCEPTED.

Implemented by: Germinate (POST only), Cassavabase

Used by: Flapjack (POST only)

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

Use POST when parameter size is greater than 2K bytes.

- If no format is specified, this call returns the data in JSON form.

- If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the "datafiles" field of the "metadata".

- If more than one format is requested at a time, the server will throw a "501 Not Implemented" error.

The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats) 

+ Parameters
 
+ Request (application/json)
/definitions/alleleMatrixSearchRequest

+ Response 200 (application/tsv)
```
{
    "result": {
        "data": []
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": [
            "https://my-fancy-server/files/allelematrix-1234.tsv"
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Markerprofiles [Get /brapi/v1/markerprofiles{?germplasmDbId}{?studyDbId}{?sampleDbId}{?extractDbId}{?pageSize}{?page}]

<strong>Scope</strong>: GENOTYPING.
<strong>Status</strong>: ACCEPTED.
<strong>Implemented by</strong>: Germinate
<strong>Used by</strong>: Flapjack
</br>
For the requested Germplasm Id and/or Extract Id, returns the Markerprofile Id and number of non-missing allele calls (marker/allele pairs). 

+ Parameters
    + germplasmDbId (Optional, string) ... The server's internal ids for the Germplasm IDs, as returned by the <strong>Find markerprofile by Germplasm</strong> service.
    + studyDbId (Optional, string) ... The server's internal id for the StudyDbId
    + sampleDbId (Optional, string) ... The server's internal id for the SampleDbId
    + extractDbId (Optional, string) ... The server's internal id for the ExtractDbId
    + pageSize (Optional, integer) ... The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    + page (Optional, integer) ... Required if `pageSize` is given; and requires that `pageSize` be given. The page indexing starts at 0 (the first page is 'page'=0)


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "uniqueDisplayName": "MyFancyGermplasm",
                "markerprofileDbId": "993",
                "resultCount": 1470,
                "sampleDbId": "3937",
                "germplasmDbId": "01BEL084609S",
                "analysisMethod": "GoldenGate",
                "extractDbId": "3939"
            },
            {
                "uniqueDisplayName": "Germplasm2",
                "markerprofileDbId": "994",
                "resultCount": 1470,
                "sampleDbId": "1234",
                "germplasmDbId": "2374",
                "analysisMethod": "GBS",
                "extractDbId": "3939"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```

## Allelematrices [Get /brapi/v1/allelematrices{?studyDbId}{?pageSize}{?page}]

<strong>Status</strong>: Proposed
<strong>Implemented by</strong>: GOBII
<strong>Used by</strong>: Flapjack
</br>
This resource is used for reading and writing genomic matrices:
</br>
GET provides a list of available matrices, optionally filtered by study;
POST will provide a means for adding new matrices (content TBD). 

+ Parameters
    + studyDbId (Required, string) ... restricts the list of matrices to a specific study.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "studyDbId": "abc123",
                "description": "a test dataset",
                "name": "testDs1",
                "lastUpdated": "2017-06-12",
                "matrixDbId": "27"
            },
            {
                "studyDbId": "abc123",
                "description": "a second test dataset",
                "name": "testDs2",
                "lastUpdated": "2017-06-12",
                "matrixDbId": "28"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```