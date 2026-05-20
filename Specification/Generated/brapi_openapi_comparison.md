#### What's Deleted
---

##### `GET` /commoncropnames


##### `POST` /delete/images


##### `POST` /delete/observations


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


###### Return Type:

New response : **404**

##### `GET` /germplasm/{germplasmDbId}/mcpd


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `germplasmPUI`

##### `PUT` /samples


###### Return Type:

Deleted response : **404**

##### `POST` /search/allelematrix


###### Request:

* Changed content type : `application/json`

    New properties: `dimensionCallSetPage`, `dimensionCallSetPageSize`, `dimensionVariantPage`, `dimensionVariantPageSize`

    * Changed property `dataMatrixAbbreviations` (array -> string):
      - Type changed: `array` -> `string`

    * Changed property `dataMatrixNames` (array -> string):
      - Type changed: `array` -> `string`

##### `POST` /search/calls


###### Request:

* Changed content type : `application/json`

    * Changed property `pageToken` (string):
      - Deprecated status changed

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

##### `POST` /search/variants


###### Request:

* Changed content type : `application/json`

    Deleted properties: `pageToken`

##### `GET` /search/variants/{searchResultsDbId}


###### Parameters:

Deleted: `pageToken` in `query`

##### `POST` /search/variantsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`

                Deleted properties: `availableFormats`, `studyDbId`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `true`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New required properties:
                        - `analysisDbId`

##### `GET` /search/variantsets/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`

                Deleted properties: `availableFormats`, `studyDbId`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `true`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New required properties:
                        - `analysisDbId`

##### `GET` /seedlots/{seedLotDbId}/transactions


###### Parameters:

Deleted: `transactionDbId` in `query`

Deleted: `transactionDirection` in `query`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `fromSeedLotPUI`, `toSeedLotPUI`

##### `GET` /trials


###### Parameters:

Deleted: `sortBy` in `query`

Deleted: `sortOrder` in `query`

##### `GET` /variantsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`

                Deleted properties: `availableFormats`, `studyDbId`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `true`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New required properties:
                        - `analysisDbId`

##### `GET` /variantsets/{variantSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `referenceSetName`

        Deleted properties: `availableFormats`, `studyDbId`

        * Changed property `referenceSetDbId` (string):
          - Nullable changed: `false` -> `true`

        * Changed property `analysis` (array)

            Changed items (array):

                New required properties:
                - `analysisDbId`

##### `POST` /attributes


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `false`

            New properties: `ontologyPUI`, `ontologyReferenceDbId`

##### `PUT` /attributes/{attributeDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `false`

        New properties: `ontologyPUI`, `ontologyReferenceDbId`

##### `POST` /images


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `imageContent`, `observationUnitName`

        Deleted properties: `observationDbIds`

        * Changed property `mimeType` (string):
          - Pattern changed: `image/.*` -> `null`

        * Changed property `imageLocation` (object)

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

##### `PUT` /images/{imageDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `imageContent`, `observationUnitName`

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

        New properties: `observationVariablePUI`, `seasonDbId`, `seasonName`, `seasonPUI`, `studyName`

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

        New properties: `crossPUI`, `locationPUI`, `programPUI`, `seedLotPUI`

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

                Deleted properties: `germplasmPUI`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /pedigree


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        Deleted properties: `germplasmPUI`

        * Changed property `parents` (array)

            Changed items (array):

                New required properties:
                - `germplasmName`

                * Changed property `germplasmName` (string):
                  - Nullable changed: `true` -> `null`

###### Return Type:

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `germplasmPUI`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /search/images


###### Request:

* Changed content type : `application/json`

    * Changed property `imageLocation` (object)

        New properties: `germplasmOrigin`, `imageDbId`, `imageName`, `imagePUI`, `observationDbId`, `observationName`, `observationPUI`, `observationUnit`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates` (object):
      - Nullable changed: `true` -> `null`

        New properties: `germplasmOrigin`, `imageDbId`, `imageName`, `imagePUI`, `observationDbId`, `observationName`, `observationPUI`, `observationUnit`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `germplasmPUI`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `GET` /search/pedigree/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `germplasmPUI`

                * Changed property `parents` (array)

                    Changed items (array):

                        New required properties:
                        - `germplasmName`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /variables


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `false`

            New properties: `ontologyPUI`, `ontologyReferenceDbId`

##### `PUT` /variables/{observationVariableDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `false`

        New properties: `ontologyPUI`, `ontologyReferenceDbId`

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

