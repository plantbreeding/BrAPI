## Get Trial By Id [/brapi/v1/trials/{trialDbId}]

Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target date: PAG2016.

Get trial by id.

###### Response data types

| Variable                | Datatype        | Description                                             | Required |
| ----------------------- | --------------- | ------------------------------------------------------- | :------: |
| trialDbId               | string          | string database identifier, not necessarily a Primary Key |    Y     |
| trialName               | string          | Human readable name                                     |    Y     |
| programDbId             | string          | string database identifier, not necessarily a Primary Key |          |
| programName             | string          |                                                         |          |
| startDate               | string          |                                                         |          |
| endDate                 | string          |                                                         |          |
| active                  | boolean         |                                                         |          |
| datasetAuthorship       | array of object | List of studies                                         |          |
| datasetAuthorship.license  | string          | License for data use. If using a known license like CC-BY, use the URI (https://creativecommons.org/licenses/by/4.0/) |          |
| datasetAuthorship.datasetPUI       | string          | DOI or any other citation mechanism for this dataset |          |
| studies                 | array of object | List of studies                                         |          |
| studies.studyDbId       | string          | Study database identifier                               |          |
| studies.studyName       | string          | Study  name                                             |          |
| studies.locationName    | string          | Study location name                                     |          |
| studies.locationDbId    | string          | Study location email                                    |          |
| contacts                | array of object | List of trial identifier                                |          |
| contacts.contactDbId    | string          | Study contact database identifier                       |          |
| contacts.name           | string          | Study contact name                                      |          |
| contacts.instituteName  | string          | Study contact institute name                            |          |
| contacts.email          | string          | Study contact email                                     |          |
| contacts.type           | string          | Study contact type (ex: Coordinator, Scientist, etc.)   |          |
| contacts.orcid          | string          | Study contact orcid identifier (http://orcid.org)       |          |
| additionalInfo          | object          | Additional arbitrary info on the trial like publications|          |
| additionalInfo.publications  | array of string | Additional info for publications                   |          |


### Get trial by Id [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "trialDbId" : 1,
                "trialName" : "InternationalTrialA",
                "programDbId": 27,
                "programName": "International Yield Trial",
                "startDate": "2007-06-01",
                "endDate"  : "2008-12-31",
                "active" : "true", 
                "datasetAuthorship":{
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI":"doi:10.15454/312953986E3"
                },
                "contacts": [
                    {
                        "contactDbId": "C025",
                        "name": "John Doe",
                        "instituteName":"IRRI",
                        "email": "j.doe@mail.com",
                        "type": "Scientist",
                        "orcid": "0000-0002-0607-8728"
                    }, {
                        "contactDbId": "C026",
                        "name": "Dave Peters",
                        "instituteName":"IRRI",
                        "email": null,
                        "type": null,
                        "orcid": null
                    }
                ],
                "studies" : [
                    {
                        "studyDbId" : 1,
                        "studyName" : "Zimbabwe Yield Trial",
                        "locationName" : "Zimbabwe",
                        "locationDbId" : "z-2"
                    },
                    {
                        "studyDbId" : 2,
                        "studyName" : "Kenya Yield Trial",
                        "locationName" : "Kenya",
                        "locationDbId" : "k-1"
                    }
                ],
                "additionalInfo" : {
                    "publications" : ["pmid:239823988","doi:10.2345/GEZG3T23535"]
                    "property2Name" : "property2Value",
                    "property3Name" : "property3Value"
                }
            }
        }        
