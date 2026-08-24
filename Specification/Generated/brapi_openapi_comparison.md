#### What's Changed
---

##### `GET` /observationunits/{observationUnitDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result`

        Deleted properties: `observations`

##### `PUT` /observationunits/{observationUnitDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result`

        Deleted properties: `observations`

##### `GET` /referencesets/{referenceSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result`

        New properties: `referencesDbId`, `referencesName`, `sourceGermplasmDbIds`, `variantDbIds`, `variantSetDbIds`

        Deleted properties: `sourceGermplasm`

##### `GET` /samples/{sampleDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result`

        New properties: `sampleDbId`

