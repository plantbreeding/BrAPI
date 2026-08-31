#### What's Deleted
---

##### `POST` /search/variables


##### `GET` /search/variables/{searchResultsDbId}


##### `GET` /variables


##### `POST` /variables


##### `GET` /variables/{observationVariableDbId}


##### `PUT` /variables/{observationVariableDbId}


#### What's Changed
---

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates` (object -> null):
      - Type changed: `object` -> `null`

##### `POST` /observations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `observationVariable`

        Deleted properties: `observationVariableDbId`, `observationVariableName`

##### `PUT` /observations/{observationDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `observationVariable`

    Deleted properties: `observationVariableDbId`, `observationVariableName`

