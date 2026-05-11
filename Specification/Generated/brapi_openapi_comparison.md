#### What's Deleted
---

##### `GET` /allelematrix


##### `GET` /commoncropnames


##### `POST` /delete/images


##### `POST` /delete/observations


##### `GET` /observationlevels


##### `GET` /observations/table


##### `GET` /observationunits/table


##### `GET` /seedlots/transactions


##### `POST` /seedlots/transactions


##### `GET` /seedlots/{seedLotDbId}/transactions


##### `GET` /serverinfo


##### `POST` /variantsets/extract


##### `PUT` /observations/{observationDbId}


##### `PUT` /observationunits/{observationUnitDbId}


##### `PUT` /calls


##### `PUT` /plates


##### `PUT` /pedigree


#### What's Changed
---

##### `GET` /markerpositions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `variantName`

##### `GET` /referencesets


###### Parameters:

Added: `externalReferenceID` in `query`

##### `POST` /search/allelematrix


###### Request:

* Changed content type : `application/json`

    * Changed property `preview` (boolean):
      - Default changed: `false` -> `none`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `data`

        Deleted properties: `callSetDbIds`, `dataMatrices`, `expandHomozygotes`, `pagination`, `sepPhased`, `sepUnphased`, `unknownString`, `variantDbIds`, `variantSetDbIds`

        New required properties:
        - `data`

        Removed required properties:
        - `callSetDbIds`
        - `variantSetDbIds`

##### `GET` /search/allelematrix/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `data`

        Deleted properties: `callSetDbIds`, `dataMatrices`, `expandHomozygotes`, `pagination`, `sepPhased`, `sepUnphased`, `unknownString`, `variantDbIds`, `variantSetDbIds`

        New required properties:
        - `data`

        Removed required properties:
        - `callSetDbIds`
        - `variantSetDbIds`

##### `POST` /search/attributes


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `studyDbId` (array):
      - Deprecated status changed

##### `GET` /search/attributes/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/attributevalues


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/attributevalues/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/germplasm


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/germplasm/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `GET` /search/images/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/lists


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `listType` (string):
      - Nullable changed: `true` -> `null`

##### `GET` /search/lists/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `GET` /search/locations/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/markerpositions


###### Request:

* Changed content type : `application/json`

    Deleted properties: `page`, `pageSize`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `variantName`

##### `GET` /search/markerpositions/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `variantName`

##### `GET` /search/observations/{searchResultsDbId}


###### Parameters:

Deleted: `Accept` in `header`

###### Return Type:

Deleted response : **202**

##### `GET` /search/observationunits/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/people


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/people/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/plates


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/plates/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/programs


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/programs/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/referencesets


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/referencesets/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/samples


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/samples/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/studies


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `sortBy` (string):
      - Removed enum values: [germplasmDbId, observationVariableDbId]

    * Changed property `sortOrder` (string):
      - Added enum values: [asc, desc]

##### `GET` /search/studies/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/trials


###### Request:

* Changed content type : `application/json`

    New properties: `observationVariablePUIs`, `observationVariableNames`, `observationVariableDbIds`, `sortOrder`, `sortBy`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

##### `GET` /search/trials/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `POST` /search/variables


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `studyDbId` (array):
      - Deprecated status changed

##### `GET` /search/variables/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

##### `GET` /seasons


###### Parameters:

Changed: `year` in `query`:
  - Type changed: `integer` -> `string`

##### `POST` /attributevalues


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `attributePUI`, `germplasmPUI`

        * Changed property `attributeDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `attributeName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /attributevalues/{attributeValueDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `attributePUI`, `germplasmPUI`

    * Changed property `attributeDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `attributeName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `germplasmDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `germplasmName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

##### `GET` /calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /callsets


###### Parameters:

Added: `externalReferenceID` in `query`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sampleName`, `samplePUI`, `studyName`, `studyPUI`

                Deleted properties: `variantSetDbIds`

                * Changed property `sampleDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /callsets/{callSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `sampleName`, `samplePUI`, `studyName`, `studyPUI`

        Deleted properties: `variantSetDbIds`

        * Changed property `sampleDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `GET` /callsets/{callSetDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /crosses


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        Deleted properties: `pollinationTimeStamp`

        * Changed property `crossType` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossingProjectDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossingProjectName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `plannedCrossDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `plannedCrossName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossAttributes` (array)

            Changed items (array):

                New properties: `crossDbId`, `crossName`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `parent1` (object):
          - Nullable changed: `true` -> `null`

            New properties: `germplasmPUI`, `observationUnitPUI`

            * Changed property `parentType` (string):
              - Added enum values: [CLONAL]

        * Changed property `pollinationEvents` (array)

            Changed items (array):

                New properties: `crossDbId`, `crossName`

##### `POST` /crossingprojects


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `potentialParents` (array)

            Changed items (array):

                New properties: `germplasmPUI`, `observationUnitPUI`

                * Changed property `parentType` (string):
                  - Added enum values: [CLONAL]

##### `PUT` /crossingprojects/{crossingProjectDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `programDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `programName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `potentialParents` (array)

        Changed items (array):

            New properties: `germplasmPUI`, `observationUnitPUI`

            * Changed property `parentType` (string):
              - Added enum values: [CLONAL]

##### `GET` /events


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `studyPUI`

                Deleted properties: `date`, `observationUnitDbIds`

                * Changed property `eventDateRange` (object -> array):
                  - Type changed: `object` -> `array`

                * Changed property `eventType` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `studyName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `eventParameters` (array)

                    Changed items (array):

                        New properties: `eventDbId`

                        Deleted properties: `key`, `rdfValue`

##### `POST` /germplasm


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `sampleDbIds`

        * Changed property `breedingMethodDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `breedingMethodName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `donors` (array)

            Changed items (array):

                New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `germplasmOrigin` (array)

            Changed items (array):

                New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

                * Changed property `coordinates` (object -> array):
                  - Type changed: `object` -> `array`

        * Changed property `storageTypes` (array)

            Changed items (array):

                New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

        * Changed property `synonyms` (array)

            Changed items (array):

                New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

        * Changed property `taxonIds` (array)

            Changed items (array):

                New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

##### `PUT` /germplasm/{germplasmDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `sampleDbIds`

    * Changed property `breedingMethodDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `breedingMethodName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `donors` (array)

        Changed items (array):

            New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `germplasmOrigin` (array)

        Changed items (array):

            New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

            * Changed property `coordinates` (object -> array):
              - Type changed: `object` -> `array`

    * Changed property `storageTypes` (array)

        Changed items (array):

            New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

    * Changed property `synonyms` (array)

        Changed items (array):

            New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

    * Changed property `taxonIds` (array)

        Changed items (array):

            New properties: `germplasmDbId`, `germplasmName`, `germplasmPUI`

##### `GET` /germplasm/{germplasmDbId}/mcpd


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `germplasmName`

        New required properties:
        - `commonCropName`
        - `germplasmDbId`
        - `germplasmName`
        - `germplasmPUI`

        * Changed property `germplasmPUI` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `breedingInstitutes` (array)

            Changed items (array):

                New properties: `instituteAddress`

##### `POST` /lists


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `personDbId`

        Deleted properties: `listOwnerPersonDbId`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /lists/{listDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `personDbId`

    Deleted properties: `listOwnerPersonDbId`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

##### `POST` /observationunits


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `germplasmPUI`, `studyPUI`, `trialPUI`

        * Changed property `crossDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `locationDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `locationName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationUnitPosition` (object -> array):
          - Type changed: `object` -> `array`

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `seedLotDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `seedLotName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `trialDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `trialName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `treatments` (array)

            Changed items (array):

                New properties: `observationUnitDbId`, `observationUnitName`, `observationUnitPUI`

##### `POST` /people


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /people/{personDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

##### `GET` /plannedcrosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                * Changed property `crossType` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array)

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parent1` (object):
                  - Nullable changed: `true` -> `null`

                    New properties: `germplasmPUI`, `observationUnitPUI`

                    * Changed property `parentType` (string):
                      - Added enum values: [CLONAL]

##### `PUT` /plannedcrosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                * Changed property `crossType` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array)

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parent1` (object):
                  - Nullable changed: `true` -> `null`

                    New properties: `germplasmPUI`, `observationUnitPUI`

                    * Changed property `parentType` (string):
                      - Added enum values: [CLONAL]

##### `POST` /plannedcrosses


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `plannedCrossDbId`

        New required properties:
        - `plannedCrossDbId`

        * Changed property `crossType` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossingProjectDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossingProjectName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `parent1` (object):
          - Nullable changed: `true` -> `null`

            New properties: `germplasmPUI`, `observationUnitPUI`

            * Changed property `parentType` (string):
              - Added enum values: [CLONAL]

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                * Changed property `crossType` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array)

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parent1` (object):
                  - Nullable changed: `true` -> `null`

                    New properties: `germplasmPUI`, `observationUnitPUI`

                    * Changed property `parentType` (string):
                      - Added enum values: [CLONAL]

##### `POST` /plates


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `programName`, `studyName`, `studyPUI`, `trialName`, `trialPUI`

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `trialDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `GET` /programs


###### Parameters:

Changed: `programType` in `query`:
  - Added enum values: [STANDARD]
  - Removed enum values: [STANARD]

##### `POST` /programs


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `personDbId`

        Deleted properties: `leadPersonDbId`, `leadPersonName`

        * Changed property `programType` (string):
          - Nullable changed: `null` -> `true`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /programs/{programDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `personDbId`

    Deleted properties: `leadPersonDbId`, `leadPersonName`

    * Changed property `programType` (string):
      - Nullable changed: `null` -> `true`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

##### `GET` /references


###### Parameters:

Added: `externalReferenceID` in `query`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sourceGermplasmDbIds`, `variantDbIds`

                Deleted properties: `sourceGermplasm`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /references/{referenceDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `sourceGermplasmDbIds`, `variantDbIds`

        Deleted properties: `sourceGermplasm`

        * Changed property `referenceSetDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `referenceSetName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /samples


###### Return Type:

Deleted response : **404**

##### `POST` /samples


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `callSetDbIds`, `germplasmName`, `germplasmPUI`, `observationUnitName`, `observationUnitPUI`, `programName`, `sampleGroupId`, `studyName`, `studyPUI`, `trialName`, `trialPUI`

        Deleted properties: `sampleGroupDbId`

        * Changed property `germplasmDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationUnitDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `plateDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `plateName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `trialDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `POST` /search/calls


###### Request:

* Changed content type : `application/json`

    Deleted properties: `page`, `pageSize`, `pageToken`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /search/calls/{searchResultsDbId}


###### Parameters:

Deleted: `pageToken` in `query`

###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /search/callsets


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sampleName`, `samplePUI`, `studyName`, `studyPUI`

                Deleted properties: `variantSetDbIds`

                * Changed property `sampleDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /search/callsets/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sampleName`, `samplePUI`, `studyName`, `studyPUI`

                Deleted properties: `variantSetDbIds`

                * Changed property `sampleDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /search/observations


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `observationDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `observationTimeStampRangeEnd` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `observationTimeStampRangeStart` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `observationUnitDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `seasonDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `observationLevelRelationships` (array):
      - Nullable changed: `true` -> `null`

        Changed items (array):

            New properties: `observationUnitName`, `observationUnitPUI`

            * Changed property `observationUnitDbId` (string):
              - Nullable changed: `true` -> `null`

    * Changed property `observationLevels` (array):
      - Nullable changed: `true` -> `null`

##### `POST` /search/observationunits


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `includeObservations` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `observationUnitDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `observationUnitNames` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `seasonDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `observationLevelRelationships` (array):
      - Nullable changed: `true` -> `null`

        Changed items (array):

            New properties: `observationUnitName`, `observationUnitPUI`

            * Changed property `observationUnitDbId` (string):
              - Nullable changed: `true` -> `null`

    * Changed property `observationLevels` (array):
      - Nullable changed: `true` -> `null`

##### `POST` /search/references


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `accessions` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `isDerived` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `md5checksums` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `referenceDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `referenceSetDbIds` (array):
      - Nullable changed: `true` -> `null`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sourceGermplasmDbIds`, `variantDbIds`

                Deleted properties: `sourceGermplasm`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /search/references/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sourceGermplasmDbIds`, `variantDbIds`

                Deleted properties: `sourceGermplasm`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /search/variants


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`, `pageToken`

    * Changed property `callSetDbIds` (array):
      - Nullable changed: `true` -> `null`
      - Deprecated status changed

    * Changed property `referenceDbId` (string):
      - Nullable changed: `true` -> `null`
      - Deprecated status changed

    * Changed property `referenceDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `referenceSetDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `variantDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `variantSetDbIds` (array):
      - Nullable changed: `true` -> `null`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `analysis`, `variantSetName`

                Deleted properties: `alternateBases`, `alternate_bases`

                * Changed property `referenceDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantSetDbId` (array -> string):
                  - Type changed: `array` -> `string`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /search/variants/{searchResultsDbId}


###### Parameters:

Deleted: `pageToken` in `query`

###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `analysis`, `variantSetName`

                Deleted properties: `alternateBases`, `alternate_bases`

                * Changed property `referenceDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantSetDbId` (array -> string):
                  - Type changed: `array` -> `string`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /search/variantsets


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`, `studyName`, `studyPUI`

                Deleted properties: `availableFormats`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        New required properties:
                        - `analysisDbId`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `metadataFields` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /search/variantsets/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`, `studyName`, `studyPUI`

                Deleted properties: `availableFormats`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        New required properties:
                        - `analysisDbId`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `metadataFields` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /seedlots


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `transactions`

        * Changed property `locationDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `locationName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `contentMixture` (array)

            Changed items (array):

                New properties: `germplasmPUI`, `seedLotDbId`, `seedLotName`

                * Changed property `crossDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmName` (string):
                  - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `PUT` /seedlots/{seedLotDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `transactions`

    * Changed property `locationDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `locationName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `programDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `programName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `contentMixture` (array)

        Changed items (array):

            New properties: `germplasmPUI`, `seedLotDbId`, `seedLotName`

            * Changed property `crossDbId` (string):
              - Nullable changed: `true` -> `null`

            * Changed property `crossName` (string):
              - Nullable changed: `true` -> `null`

            * Changed property `germplasmDbId` (string):
              - Nullable changed: `true` -> `null`

            * Changed property `germplasmName` (string):
              - Nullable changed: `true` -> `null`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

##### `POST` /studies


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `trialPUI`

        Deleted properties: `contacts`, `observationVariableDbIds`

        * Changed property `locationDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `locationName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDescription` (string):
          - Nullable changed: `null` -> `true`

        * Changed property `studyName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `environmentParameters` (array)

            Changed items (array):

                New properties: `environmentParametersDbId`, `studyDbId`, `studyName`, `studyPUI`

                New required properties:
                - `environmentParametersDbId`

        * Changed property `experimentalDesign` (object):
          - Nullable changed: `true` -> `null`

            New properties: `studyDbId`, `studyName`, `studyPUI`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `growthFacility` (object):
          - Nullable changed: `true` -> `null`

            * Changed property `PUI` (string):
              - Nullable changed: `null` -> `true`

        * Changed property `lastUpdate` (object):
          - Nullable changed: `true` -> `null`

            New properties: `lastUpdateDbId`, `studyDbId`, `studyName`, `studyPUI`

            New required properties:
            - `lastUpdateDbId`

##### `PUT` /studies/{studyDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `trialPUI`

    Deleted properties: `contacts`, `observationVariableDbIds`

    * Changed property `locationDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `locationName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `studyDescription` (string):
      - Nullable changed: `null` -> `true`

    * Changed property `studyName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `environmentParameters` (array)

        Changed items (array):

            New properties: `environmentParametersDbId`, `studyDbId`, `studyName`, `studyPUI`

            New required properties:
            - `environmentParametersDbId`

    * Changed property `experimentalDesign` (object):
      - Nullable changed: `true` -> `null`

        New properties: `studyDbId`, `studyName`, `studyPUI`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `growthFacility` (object):
      - Nullable changed: `true` -> `null`

        * Changed property `PUI` (string):
          - Nullable changed: `null` -> `true`

    * Changed property `lastUpdate` (object):
      - Nullable changed: `true` -> `null`

        New properties: `lastUpdateDbId`, `studyDbId`, `studyName`, `studyPUI`

        New required properties:
        - `lastUpdateDbId`

##### `POST` /trials


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `studyDbIds`

        * Changed property `programDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `programName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `datasetAuthorships` (array)

            Changed items (array):

                New properties: `trialDbId`, `trialName`, `trialPUI`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `publications` (array)

            Changed items (array):

                New properties: `trialDbId`, `trialName`, `trialPUI`

##### `PUT` /trials/{trialDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `studyDbIds`

    * Changed property `programDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `programName` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `datasetAuthorships` (array)

        Changed items (array):

            New properties: `trialDbId`, `trialName`, `trialPUI`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `publications` (array)

        Changed items (array):

            New properties: `trialDbId`, `trialName`, `trialPUI`

##### `GET` /variants


###### Parameters:

Added: `externalReferenceID` in `query`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `analysis`, `variantSetName`

                Deleted properties: `alternateBases`, `alternate_bases`

                * Changed property `referenceDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantSetDbId` (array -> string):
                  - Type changed: `array` -> `string`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /variants/{variantDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `analysis`, `variantSetName`

        Deleted properties: `alternateBases`, `alternate_bases`

        * Changed property `referenceDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `referenceName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `referenceSetDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `referenceSetName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `variantDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `variantSetDbId` (array -> string):
          - Type changed: `array` -> `string`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

##### `GET` /variants/{variantDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /variantsets


###### Parameters:

Added: `externalReferenceID` in `query`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `referenceSetName`, `studyName`, `studyPUI`

                Deleted properties: `availableFormats`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `false` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `analysis` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        New required properties:
                        - `analysisDbId`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `metadataFields` (array)

                    Changed items (array):

                        New properties: `variantSetDbId`, `variantSetName`

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /variantsets/{variantSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        New properties: `referenceSetName`, `studyName`, `studyPUI`

        Deleted properties: `availableFormats`

        * Changed property `referenceSetDbId` (string):
          - Nullable changed: `false` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `analysis` (array)

            Changed items (array):

                New properties: `variantSetDbId`, `variantSetName`

                New required properties:
                - `analysisDbId`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `metadataFields` (array)

            Changed items (array):

                New properties: `variantSetDbId`, `variantSetName`

                * Changed property `dataType` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `fieldAbbreviation` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `fieldName` (string):
                  - Nullable changed: `null` -> `true`

##### `GET` /variantsets/{variantSetDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        Deleted properties: `expandHomozygotes`, `sepPhased`, `sepUnphased`, `unknownString`

        * Changed property `data` (array)

            Changed items (array):

                Deleted properties: `genotype`, `genotype_likelihood`, `variantName`

                * Changed property `genotypeValue` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `phaseSet` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `genotypeMetadata` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        * Changed property `dataType` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldAbbreviation` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldName` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `fieldValue` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /variantsets/{variantSetDbId}/callsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `sampleName`, `samplePUI`, `studyName`, `studyPUI`

                Deleted properties: `variantSetDbIds`

                * Changed property `sampleDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `studyDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `GET` /variantsets/{variantSetDbId}/variants


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `analysis`, `variantSetName`

                Deleted properties: `alternateBases`, `alternate_bases`

                * Changed property `referenceDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `referenceSetName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `variantSetDbId` (array -> string):
                  - Type changed: `array` -> `string`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

##### `POST` /attributes


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `attributeValueDbIds`, `methodDbId`, `methodName`, `methodPUI`, `scaleDbId`, `scaleName`, `scalePUI`, `traitDbId`, `traitName`, `traitPUI`

        Deleted properties: `method`, `scale`, `trait`

        New required properties:
        - `methodDbId`
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        Removed required properties:
        - `method`
        - `scale`
        - `trait`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `null`

            New properties: `ontologyReferenceDbId`

            * Changed property `documentationLinks` (array)

                Changed items (array):

                    * Changed property `URL` (string):
                      - Nullable changed: `null` -> `true`

                    * Changed property `type` (string):
                      - Nullable changed: `null` -> `true`

##### `PUT` /attributes/{attributeDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `attributeValueDbIds`, `methodDbId`, `methodName`, `methodPUI`, `scaleDbId`, `scaleName`, `scalePUI`, `traitDbId`, `traitName`, `traitPUI`

    Deleted properties: `method`, `scale`, `trait`

    New required properties:
    - `methodDbId`
    - `methodName`
    - `scaleDbId`
    - `scaleName`
    - `traitName`

    Removed required properties:
    - `method`
    - `scale`
    - `trait`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `null`

        New properties: `ontologyReferenceDbId`

        * Changed property `documentationLinks` (array)

            Changed items (array):

                * Changed property `URL` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `type` (string):
                  - Nullable changed: `null` -> `true`

##### `POST` /images


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `imageContent`, `observationUnitName`, `observationUnitPUI`

        Deleted properties: `observationDbIds`

        * Changed property `mimeType` (string):
          - Pattern changed: `image/.*` -> `null`

        * Changed property `observationUnitDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `imageLocation` (object):
          - Nullable changed: `true` -> `null`

            * Changed property `type` (string):
              - Default changed: `Feature` -> `none`

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

##### `PUT` /images/{imageDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `imageContent`, `observationUnitName`, `observationUnitPUI`

    Deleted properties: `observationDbIds`

    * Changed property `mimeType` (string):
      - Pattern changed: `image/.*` -> `null`

    * Changed property `observationUnitDbId` (string):
      - Nullable changed: `true` -> `null`

    * Changed property `externalReferences` (array):
      - Nullable changed: `null` -> `true`

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `imageLocation` (object):
      - Nullable changed: `true` -> `null`

        * Changed property `type` (string):
          - Default changed: `Feature` -> `none`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /locations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `childLocationDbIds`, `locationDbId`

        Deleted properties: `parentLocationDbId`, `parentLocationName`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `coordinates` (object):
          - Nullable changed: `true` -> `null`

            * Changed property `type` (string):
              - Default changed: `Feature` -> `none`

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

##### `PUT` /locations/{locationDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `childLocationDbIds`, `locationDbId`

    Deleted properties: `parentLocationDbId`, `parentLocationName`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `coordinates` (object):
      - Nullable changed: `true` -> `null`

        * Changed property `type` (string):
          - Default changed: `Feature` -> `none`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `PUT` /observations


###### Return Type:

Deleted response : **404**

##### `POST` /observations


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `germplasmPUI`, `observationUnitPUI`, `observationVariablePUI`, `seasonDbId`, `seasonName`, `studyName`, `studyPUI`

        Deleted properties: `season`

        * Changed property `germplasmDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationUnitDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationUnitName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationVariableDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `observationVariableName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `studyDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `geoCoordinates` (object):
          - Nullable changed: `true` -> `null`

            * Changed property `type` (string):
              - Default changed: `Feature` -> `none`

            * Changed property `geometry` (object -> null):
              - Type changed: `object` -> `null`

###### Return Type:

Deleted response : **404**

##### `GET` /pedigree


###### Parameters:

Added: `externalReferenceID` in `query`

###### Return Type:

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `crossingProjectName`, `pedigreeNodeDbId`, `siblingDbIds`

                Deleted properties: `siblings`

                New required properties:
                - `germplasmPUI`
                - `pedigreeNodeDbId`

                * Changed property `breedingMethodDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `breedingMethodName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmPUI` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parents` (array)

                    Changed items (array):

                        New properties: `germplasmPUI`, `pedigreeNodeDbId`

                        New required properties:
                        - `germplasmName`
                        - `germplasmPUI`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /pedigree


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `crossingProjectName`, `pedigreeNodeDbId`, `siblingDbIds`

        Deleted properties: `siblings`

        New required properties:
        - `germplasmPUI`
        - `pedigreeNodeDbId`

        * Changed property `breedingMethodDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `breedingMethodName` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `crossingProjectDbId` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `germplasmPUI` (string):
          - Nullable changed: `true` -> `null`

        * Changed property `externalReferences` (array):
          - Nullable changed: `null` -> `true`

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `parents` (array)

            Changed items (array):

                New properties: `germplasmPUI`, `pedigreeNodeDbId`

                New required properties:
                - `germplasmName`
                - `germplasmPUI`

                * Changed property `germplasmName` (string):
                  - Nullable changed: `true` -> `null`

###### Return Type:

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `crossingProjectName`, `pedigreeNodeDbId`, `siblingDbIds`

                Deleted properties: `siblings`

                New required properties:
                - `germplasmPUI`
                - `pedigreeNodeDbId`

                * Changed property `breedingMethodDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `breedingMethodName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmPUI` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parents` (array)

                    Changed items (array):

                        New properties: `germplasmPUI`, `pedigreeNodeDbId`

                        New required properties:
                        - `germplasmName`
                        - `germplasmPUI`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /search/images


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `imageLocation` (object)

        New properties: `germplasmOrigin`, `imageDbId`, `imageName`, `observationDbId`, `observationUnit`

        * Changed property `type` (string):
          - Default changed: `Feature` -> `none`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `abbreviations` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `altitudeMax` (number):
      - Nullable changed: `true` -> `null`

    * Changed property `altitudeMin` (number):
      - Nullable changed: `true` -> `null`

    * Changed property `countryCodes` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `countryNames` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `instituteAddresses` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `instituteNames` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `locationTypes` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `parentLocationDbIds` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `parentLocationNames` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `coordinates` (object):
      - Nullable changed: `true` -> `null`

        New properties: `germplasmOrigin`, `imageDbId`, `imageName`, `observationDbId`, `observationUnit`

        * Changed property `type` (string):
          - Default changed: `Feature` -> `none`

        * Changed property `geometry` (object -> null):
          - Type changed: `object` -> `null`

##### `POST` /search/pedigree


###### Request:

* Changed content type : `application/json`

    Deleted properties: `externalReferenceIDs`, `externalReferenceIds`, `externalReferenceSources`, `page`, `pageSize`

    * Changed property `accessionNumbers` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `binomialNames` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `collections` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `familyCodes` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `genus` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `germplasmPUIs` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `includeFullTree` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `includeParents` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `includeProgeny` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `includeSiblings` (boolean):
      - Nullable changed: `true` -> `null`

    * Changed property `instituteCodes` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `species` (array):
      - Nullable changed: `true` -> `null`

    * Changed property `synonyms` (array):
      - Nullable changed: `true` -> `null`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `crossingProjectName`, `pedigreeNodeDbId`, `siblingDbIds`

                Deleted properties: `siblings`

                New required properties:
                - `germplasmPUI`
                - `pedigreeNodeDbId`

                * Changed property `breedingMethodDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `breedingMethodName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmPUI` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parents` (array)

                    Changed items (array):

                        New properties: `germplasmPUI`, `pedigreeNodeDbId`

                        New required properties:
                        - `germplasmName`
                        - `germplasmPUI`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `GET` /search/pedigree/{searchResultsDbId}


###### Return Type:

Deleted response : **202**

Deleted response : **404**

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (array):

                New properties: `crossingProjectName`, `pedigreeNodeDbId`, `siblingDbIds`

                Deleted properties: `siblings`

                New required properties:
                - `germplasmPUI`
                - `pedigreeNodeDbId`

                * Changed property `breedingMethodDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `breedingMethodName` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `crossingProjectDbId` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `germplasmPUI` (string):
                  - Nullable changed: `true` -> `null`

                * Changed property `externalReferences` (array):
                  - Nullable changed: `null` -> `true`

                    Changed items (array):

                        Deleted properties: `referenceID`

                        * Changed property `referenceId` (string):
                          - Nullable changed: `null` -> `true`

                        * Changed property `referenceSource` (string):
                          - Nullable changed: `null` -> `true`

                * Changed property `parents` (array)

                    Changed items (array):

                        New properties: `germplasmPUI`, `pedigreeNodeDbId`

                        New required properties:
                        - `germplasmName`
                        - `germplasmPUI`

                        * Changed property `germplasmName` (string):
                          - Nullable changed: `true` -> `null`

##### `POST` /variables


###### Request:

* Changed content type : `application/json`

    Changed items (array):

        New properties: `methodDbId`, `methodName`, `methodPUI`, `scaleDbId`, `scaleName`, `scalePUI`, `traitDbId`, `traitName`, `traitPUI`

        Deleted properties: `method`, `scale`, `trait`

        New required properties:
        - `methodDbId`
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        Removed required properties:
        - `method`
        - `scale`
        - `trait`

        * Changed property `externalReferences` (array)

            Changed items (array):

                Deleted properties: `referenceID`

                * Changed property `referenceId` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `referenceSource` (string):
                  - Nullable changed: `null` -> `true`

        * Changed property `ontologyReference` (object):
          - Nullable changed: `true` -> `null`

            New properties: `ontologyReferenceDbId`

            * Changed property `documentationLinks` (array)

                Changed items (array):

                    * Changed property `URL` (string):
                      - Nullable changed: `null` -> `true`

                    * Changed property `type` (string):
                      - Nullable changed: `null` -> `true`

##### `PUT` /variables/{observationVariableDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `methodDbId`, `methodName`, `methodPUI`, `scaleDbId`, `scaleName`, `scalePUI`, `traitDbId`, `traitName`, `traitPUI`

    Deleted properties: `method`, `scale`, `trait`

    New required properties:
    - `methodDbId`
    - `methodName`
    - `scaleDbId`
    - `scaleName`
    - `traitName`

    Removed required properties:
    - `method`
    - `scale`
    - `trait`

    * Changed property `externalReferences` (array)

        Changed items (array):

            Deleted properties: `referenceID`

            * Changed property `referenceId` (string):
              - Nullable changed: `null` -> `true`

            * Changed property `referenceSource` (string):
              - Nullable changed: `null` -> `true`

    * Changed property `ontologyReference` (object):
      - Nullable changed: `true` -> `null`

        New properties: `ontologyReferenceDbId`

        * Changed property `documentationLinks` (array)

            Changed items (array):

                * Changed property `URL` (string):
                  - Nullable changed: `null` -> `true`

                * Changed property `type` (string):
                  - Nullable changed: `null` -> `true`

