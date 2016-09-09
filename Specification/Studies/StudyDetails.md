## Study Details [/brapi/v1/studies/{studyDbId}]
Scope: CORE.
Status: ACCEPTED.
Implemented by: Germinate, GnpIS

Notes: an additionalInfo field was added to provide a controlled vocabulary for less common data fields.

Retrieve the information of the study required for field data collection

More linked data:
* observation variables: ```/brapi/v1/studies/{studyDbId}/observationVariables```
* germplasm: ```/brapi/v1/studies/{studyDbId}/germplasm```
* observation units: ```/brapi/v1/studies/{studyId}/observationUnits```
* layout: ```brapi/v1/studies/{studyDbId}/layout```

###### Response data types

| Variable                | Datatype        | Description                                             | Required |
| ----------------------- | --------------- | ------------------------------------------------------- | :------: |
| studyDbId               | string          | string database identifier                              |    Y     |
| studyName               | string          | Human readable name                                     |    Y     |
| studyType               | string          | Human readable name                                     |          |
| seasons                 | array of string | list of seasons the trials is running                   |          |
| trialDbId               | string          | Study trial database identifier                         |    Y     |
| trialName               | string          | Study trial name                                        |    Y     |
| startDate               | string          | Study start date (format YYYY-MM-DD)                    |          |
| endDate                 | string          | Study end date (format YYYY-MM-DD)                      |          |
| active                  | boolean         | Study active status (true/false)                        |          |
| location                | object          | Study location metadata object                          |    Y     |
| location.locationDbId   | string          | Study location database identifier                      |    Y     |
| location.name           | string          | Study location name                                     |    Y     |
| location.abbreviation   | string          | Study location abbreviation                             |          |
| location.countryCode    | string          | Study location ISO-3166 country code (ex: US, FR, etc.) |          |
| location.countryName    | string          | Study location country                                  |          |
| location.latitude       | number          | Study location latitude                                 |          |
| location.longitude      | number          | Study location longitude                                |          |
| location.altitude       | number          | Study location altitude in meters                       |          |
| location.additionalInfo | object          | Additional arbitrary info on the study location         |          |
| additionalInfo          | object          | Additional arbitrary info on the study                  |          |

### Retrieve study details [GET]

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": null,
                "status": null,
                "datafiles": []
            },
            "result": {
                "studyDbId": 35,
                "studyName": "Earlygenerationtesting",
                "studyType": "Yield study",
                "seasons": [
                    "2005 Winter",
                    "2008 Summer"
                ],
                "trialDbId": 57,
                "trialName": "International Yield Trial",
                "startDate": "2005-06-01",
                "endDate": "2008-12-31",
                "active": "true",
                "location": {
                    "locationDbId": 1,
                    "name": "Ibadan",
                    "abbreviation": "IB",
                    "countryCode": "NGA",
                    "countryName": "Nigeria",
                    "latitude": -21.5,
                    "longitude": 165.5,
                    "altitude": 12,
                    "additionalInfo": {
                        "AnnualMeanRain": "value",
                        "SoilDescription": "23",
                        "property1Name": "property1Value",
                        "property2Name": "property2Value"
                    }
                },
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "principalInvestigator": "Dr. Breeder",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                }
            }
        }
