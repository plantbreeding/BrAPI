#### What's Deleted
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

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates` (object -> null):
      - Type changed: `object` -> `null`

##### `GET` /allelematrix


###### Return Type:

New response : **404**

##### `POST` /attributes


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object -> null):
          - Type changed: `object` -> `null`

##### `PUT` /attributes/{attributeDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object -> null):
      - Type changed: `object` -> `null`

##### `PUT` /samples


###### Return Type:

Deleted response : **404**

##### `POST` /search/allelematrix


###### Request:

* Changed content type : `application/json`

    * Changed property `dataMatrixAbbreviations` (array -> string):
      - Type changed: `array` -> `string`

    * Changed property `dataMatrixNames` (array -> string):
      - Type changed: `array` -> `string`

##### `GET` /seedlots/{seedLotDbId}/transactions


###### Parameters:

Deleted: `transactionDbId` in `query`

##### `POST` /variables


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `ontologyReference` (object -> null):
          - Type changed: `object` -> `null`

##### `PUT` /variables/{observationVariableDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference` (object -> null):
      - Type changed: `object` -> `null`

##### `POST` /images


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        Deleted properties: `observationDbIds`

        * Changed property `mimeType` (string):
          - Pattern changed: `image/.*` -> `null`

        * Changed property `imageLocation` (object)

            * Changed property `geometry` (object):
              - Discriminator property changed

##### `PUT` /images/{imageDbId}


###### Request:

* Changed content type : `application/json`

    Deleted properties: `observationDbIds`

    * Changed property `mimeType` (string):
      - Pattern changed: `image/.*` -> `null`

    * Changed property `imageLocation` (object)

        * Changed property `geometry` (object):
          - Discriminator property changed

##### `POST` /locations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `coordinates` (object)

            * Changed property `geometry` (object):
              - Discriminator property changed

##### `PUT` /locations/{locationDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates` (object)

        * Changed property `geometry` (object):
          - Discriminator property changed

##### `PUT` /observations


###### Return Type:

Deleted response : **404**

##### `POST` /observations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `season` (object -> null):
          - Type changed: `object` -> `null`

        * Changed property `geoCoordinates` (object)

            * Changed property `geometry` (object):
              - Discriminator property changed

###### Return Type:

Deleted response : **404**

##### `POST` /observationunits


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `observationUnitPosition` (object)

            * Changed property `geoCoordinates` (object -> array):
              - Type changed: `object` -> `array`

            * Changed property `positionCoordinateXType` (string -> null):
              - Type changed: `string` -> `null`

            * Changed property `positionCoordinateYType` (string -> null):
              - Type changed: `string` -> `null`

##### `GET` /pedigree


###### Return Type:

Deleted response : **404**

##### `POST` /pedigree


###### Return Type:

Deleted response : **404**

##### `POST` /search/images


###### Request:

* Changed content type : `application/json`

    * Changed property `imageLocation` (object)

        * Changed property `geometry` (object):
          - Discriminator property changed

##### `POST` /germplasm


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `germplasmOrigin` (array)

            Changed items (array):

                * Changed property `coordinates` (object)

                    * Changed property `geometry` (object):
                      - Discriminator property changed

##### `PUT` /germplasm/{germplasmDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `germplasmOrigin` (array)

        Changed items (array):

            * Changed property `coordinates` (object)

                * Changed property `geometry` (object):
                  - Discriminator property changed

