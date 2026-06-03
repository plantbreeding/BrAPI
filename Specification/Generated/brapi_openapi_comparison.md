#### What's New
---

##### `GET` /commoncropnames


##### `POST` /delete/images


##### `POST` /delete/observations


##### `PUT` /images/{imageDbId}/imagecontent


##### `GET` /observationlevels


##### `GET` /observations/table


##### `GET` /observationunits/table


##### `GET` /seedlots/transactions


##### `POST` /seedlots/transactions


##### `GET` /serverinfo


##### `POST` /variantsets/extract


##### `PUT` /observations/{observationDbId}


##### `PUT` /observationunits/{observationUnitDbId}


##### `PUT` /calls


##### `PUT` /plates


##### `PUT` /pedigree


#### What's Changed
---

##### `POST` /search/lists


###### Request:

* Changed content type : `application/json`

    * Changed property `listType` (string):
      - Nullable changed: `true` -> `null`

##### `GET` /allelematrix


###### Parameters:

Deleted: `dataMatrixNames` in `query`

Deleted: `dataMatrixAbbreviations` in `query`

Added: `dataMatrixName` in `query`

Added: `dataMatrixAbbreviation` in `query`

###### Return Type:

New response : **404**

##### `PUT` /samples


###### Return Type:

Deleted response : **404**

##### `GET` /search/calls/{searchResultsDbId}


###### Parameters:

Deleted: `pageToken` in `query`

##### `POST` /search/observations


###### Request:

* Changed content type : `application/json`

    * Changed property `observationLevelRelationships` (array)

        Changed items (array):

            * Changed property `observationUnitDbId` (string):
              - Nullable changed: `true` -> `null`

##### `POST` /search/observationunits


###### Request:

* Changed content type : `application/json`

    * Changed property `observationLevelRelationships` (array)

        Changed items (array):

            * Changed property `observationUnitDbId` (string):
              - Nullable changed: `true` -> `null`

##### `GET` /search/variants/{searchResultsDbId}


###### Parameters:

Deleted: `pageToken` in `query`

##### `GET` /seedlots/{seedLotDbId}/transactions


###### Parameters:

Deleted: `transactionDbId` in `query`

##### `POST` /attributes


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `false`

            New properties: `ontologyReferenceDbId`

##### `PUT` /attributes/{attributeDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `false`

        New properties: `ontologyReferenceDbId`

##### `POST` /images


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        Deleted properties: `observationDbIds`

        * Changed property `mimeType` (string):
          - Pattern changed: `image/.*` -> `null`

        * Changed property `imageLocation` (object)

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

##### `PUT` /images/{imageDbId}


###### Request:

* Changed content type : `application/json`

    Deleted properties: `observationDbIds`

    * Changed property `mimeType` (string):
      - Pattern changed: `image/.*` -> `null`

    * Changed property `imageLocation` (object)

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /locations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `childLocationDbIds`, `parentLocationPUI`

        * Changed property `coordinates` (object)

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

##### `PUT` /locations/{locationDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `childLocationDbIds`, `parentLocationPUI`

    * Changed property `coordinates` (object)

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `PUT` /observations


###### Return Type:

Deleted response : **404**

##### `POST` /observations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `seasonDbId`

        Deleted properties: `season`

        * Changed property `geoCoordinates` (object)

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

###### Return Type:

Deleted response : **404**

##### `POST` /observationunits


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `observationUnitPosition` (object)

            * Changed property `geoCoordinates` (object -> array):
              - Type changed: `object` -> `array`

            * Changed property `positionCoordinateXType` (string):
              - Nullable changed: `true` -> `null`

            * Changed property `positionCoordinateYType` (string):
              - Nullable changed: `true` -> `null`

            * Changed property `observationLevelRelationships` (array)

                Changed items (array):

                    * Changed property `observationUnitDbId` (string):
                      - Nullable changed: `true` -> `null`

##### `GET` /pedigree


###### Return Type:

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New required properties:
                - `germplasmPUI`

                * Changed property `progeny` (array)

                    Changed items (array):

                        New properties: `childGermplasmDbId`, `childGermplasmName`, `pedigreeNodeDbId`, `pedigreeNodeName`, `pedigreeNodePUI`

                        Deleted properties: `germplasmDbId`, `germplasmName`

                        New required properties:
                        - `childGermplasmDbId`
                        - `childGermplasmName`

                        Removed required properties:
                        - `germplasmDbId`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

##### `POST` /pedigree


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New required properties:
        - `germplasmPUI`

        * Changed property `progeny` (array)

            Changed items (array):

                New properties: `childGermplasmDbId`, `childGermplasmName`, `pedigreeNodeDbId`, `pedigreeNodeName`, `pedigreeNodePUI`

                Deleted properties: `germplasmDbId`, `germplasmName`

                New required properties:
                - `childGermplasmDbId`
                - `childGermplasmName`

                Removed required properties:
                - `germplasmDbId`

        * Changed property `parents` (array)

            Changed items (array):

                New required properties:
                - `germplasmName`

###### Return Type:

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New required properties:
                - `germplasmPUI`

                * Changed property `progeny` (array)

                    Changed items (array):

                        New properties: `childGermplasmDbId`, `childGermplasmName`, `pedigreeNodeDbId`, `pedigreeNodeName`, `pedigreeNodePUI`

                        Deleted properties: `germplasmDbId`, `germplasmName`

                        New required properties:
                        - `childGermplasmDbId`
                        - `childGermplasmName`

                        Removed required properties:
                        - `germplasmDbId`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

##### `POST` /search/images


###### Request:

* Changed content type : `application/json`

    * Changed property `imageLocation` (object)

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates` (object):
      - Nullable changed: `true` -> `null`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New required properties:
                - `germplasmPUI`

                * Changed property `progeny` (array)

                    Changed items (array):

                        New properties: `childGermplasmDbId`, `childGermplasmName`, `pedigreeNodeDbId`, `pedigreeNodeName`, `pedigreeNodePUI`

                        Deleted properties: `germplasmDbId`, `germplasmName`

                        New required properties:
                        - `childGermplasmDbId`
                        - `childGermplasmName`

                        Removed required properties:
                        - `germplasmDbId`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

##### `GET` /search/pedigree/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New required properties:
                - `germplasmPUI`

                * Changed property `progeny` (array)

                    Changed items (array):

                        New properties: `childGermplasmDbId`, `childGermplasmName`, `pedigreeNodeDbId`, `pedigreeNodeName`, `pedigreeNodePUI`

                        Deleted properties: `germplasmDbId`, `germplasmName`

                        New required properties:
                        - `childGermplasmDbId`
                        - `childGermplasmName`

                        Removed required properties:
                        - `germplasmDbId`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

##### `POST` /variables


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `false`

            New properties: `ontologyReferenceDbId`

##### `PUT` /variables/{observationVariableDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `false`

        New properties: `ontologyReferenceDbId`

##### `POST` /germplasm


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `breedingMethodPUI`

        * Changed property `germplasmOrigin` (array)

            Changed items (array):

                * Changed property `coordinates` (object)

                    * Changed property `geometry` (object -> null):
                      - Type changed: `object` -> `null`

##### `PUT` /germplasm/{germplasmDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `breedingMethodPUI`

    * Changed property `germplasmOrigin` (array)

        Changed items (array):

            * Changed property `coordinates` (object)

                * Changed property `geometry` (object -> null):
                  - Type changed: `object` -> `null`

