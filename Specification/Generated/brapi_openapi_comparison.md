#### What's Changed
---

##### `GET` /allelematrix


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /attributes


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /attributes


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /attributes/categories


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /attributevalues


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /attributevalues


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /attributevalues/{attributeValueDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `attributeDbId`, `attributeName`, `attributeValueDbId`, `determinedDate`, `externalReferences`, `germplasmDbId`, `germplasmName`, `value`

        Removed required properties:
        - `attributeName`
        - `attributeValueDbId`

##### `PUT` /attributevalues/{attributeValueDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `attributeDbId`, `attributeName`, `attributeValueDbId`, `determinedDate`, `externalReferences`, `germplasmDbId`, `germplasmName`, `value`

        Removed required properties:
        - `attributeName`
        - `attributeValueDbId`

##### `GET` /breedingmethods


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /breedingmethods/{breedingMethodDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /calls


###### Parameters:

Added: `null` in `null`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /callsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /callsets/{callSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /callsets/{callSetDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /commoncropnames


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /crossingprojects


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /crossingprojects


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /crossingprojects/{crossingProjectDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `commonCropName`, `crossingProjectDbId`, `crossingProjectDescription`, `crossingProjectName`, `externalReferences`, `potentialParents`, `programDbId`, `programName`

        Removed required properties:
        - `crossingProjectDbId`
        - `crossingProjectName`

##### `PUT` /crossingprojects/{crossingProjectDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `commonCropName`, `crossingProjectDbId`, `crossingProjectDescription`, `crossingProjectName`, `externalReferences`, `potentialParents`, `programDbId`, `programName`

        Removed required properties:
        - `crossingProjectDbId`
        - `crossingProjectName`

##### `POST` /delete/observations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /events


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /germplasm


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /germplasm


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /germplasm/{germplasmDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `accessionNumber`, `acquisitionDate`, `additionalInfo`, `biologicalStatusOfAccessionCode`, `biologicalStatusOfAccessionDescription`, `breedingMethodDbId`, `breedingMethodName`, `collection`, `commonCropName`, `countryOfOriginCode`, `defaultDisplayName`, `documentationURL`, `donors`, `externalReferences`, `genus`, `germplasmDbId`, `germplasmName`, `germplasmOrigin`, `germplasmPUI`, `germplasmPreprocessing`, `instituteCode`, `instituteName`, `pedigree`, `seedSource`, `seedSourceDescription`, `species`, `speciesAuthority`, `storageTypes`, `subtaxa`, `subtaxaAuthority`, `synonyms`, `taxonIds`

        Removed required properties:
        - `commonCropName`
        - `germplasmDbId`
        - `germplasmName`
        - `germplasmPUI`

##### `PUT` /germplasm/{germplasmDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `accessionNumber`, `acquisitionDate`, `additionalInfo`, `biologicalStatusOfAccessionCode`, `biologicalStatusOfAccessionDescription`, `breedingMethodDbId`, `breedingMethodName`, `collection`, `commonCropName`, `countryOfOriginCode`, `defaultDisplayName`, `documentationURL`, `donors`, `externalReferences`, `genus`, `germplasmDbId`, `germplasmName`, `germplasmOrigin`, `germplasmPUI`, `germplasmPreprocessing`, `instituteCode`, `instituteName`, `pedigree`, `seedSource`, `seedSourceDescription`, `species`, `speciesAuthority`, `storageTypes`, `subtaxa`, `subtaxaAuthority`, `synonyms`, `taxonIds`

        Removed required properties:
        - `commonCropName`
        - `germplasmDbId`
        - `germplasmName`
        - `germplasmPUI`

##### `GET` /images


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /images


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /images/{imageDbId}/imagecontent


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `copyright`, `descriptiveOntologyTerms`, `externalReferences`, `imageDbId`, `imageFileName`, `imageFileSize`, `imageHeight`, `imageLocation`, `imageName`, `imageTimeStamp`, `imageURL`, `imageWidth`, `mimeType`, `observationDbIds`, `observationUnitDbId`

        Removed required properties:
        - `imageDbId`

##### `GET` /lists


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /lists


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /lists/{listDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `data`, `dateCreated`, `dateModified`, `externalReferences`, `listDbId`, `listDescription`, `listName`, `listOwnerName`, `listOwnerPersonDbId`, `listSize`, `listSource`, `listType`

        Removed required properties:
        - `listDbId`
        - `listName`
        - `listType`

##### `PUT` /lists/{listDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `data`, `dateCreated`, `dateModified`, `externalReferences`, `listDbId`, `listDescription`, `listName`, `listOwnerName`, `listOwnerPersonDbId`, `listSize`, `listSource`, `listType`

        Removed required properties:
        - `listDbId`
        - `listName`
        - `listType`

##### `POST` /lists/{listDbId}/data


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `data`, `dateCreated`, `dateModified`, `externalReferences`, `listDbId`, `listDescription`, `listName`, `listOwnerName`, `listOwnerPersonDbId`, `listSize`, `listSource`, `listType`

        Removed required properties:
        - `listDbId`
        - `listName`
        - `listType`

##### `GET` /locations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /locations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /maps


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /maps/{mapDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /maps/{mapDbId}/linkagegroups


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /markerpositions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /methods


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /methods


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /methods/{methodDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `bibliographicalReference`, `externalReferences`, `formula`, `methodClass`, `methodDbId`, `methodName`, `methodPUI`, `ontologyReference`

        Removed required properties:
        - `methodDbId`
        - `methodName`

##### `PUT` /methods/{methodDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `additionalInfo`, `bibliographicalReference`, `externalReferences`, `formula`, `methodClass`, `methodName`, `methodPUI`, `ontologyReference`

    New required properties:
    - `methodName`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `bibliographicalReference`, `externalReferences`, `formula`, `methodClass`, `methodDbId`, `methodName`, `methodPUI`, `ontologyReference`

        Removed required properties:
        - `methodDbId`
        - `methodName`

##### `GET` /observationlevels


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /observations/table


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `data`, `headerRow`, `observationVariables`

##### `GET` /observationunits/table


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `data`, `headerRow`, `observationVariables`

##### `GET` /ontologies


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /ontologies


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /ontologies/{ontologyDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `authors`, `copyright`, `documentationURL`, `licence`, `ontologyDbId`, `ontologyName`, `version`

        Removed required properties:
        - `ontologyDbId`
        - `ontologyName`

##### `PUT` /ontologies/{ontologyDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `authors`, `copyright`, `documentationURL`, `licence`, `ontologyDbId`, `ontologyName`, `version`

        Removed required properties:
        - `ontologyDbId`
        - `ontologyName`

##### `GET` /pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /people


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /people


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /people/{personDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `emailAddress`, `externalReferences`, `firstName`, `lastName`, `mailingAddress`, `middleName`, `personDbId`, `phoneNumber`, `userID`

        Removed required properties:
        - `personDbId`

##### `PUT` /people/{personDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `emailAddress`, `externalReferences`, `firstName`, `lastName`, `mailingAddress`, `middleName`, `personDbId`, `phoneNumber`, `userID`

        Removed required properties:
        - `personDbId`

##### `GET` /plates


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /plates


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /plates


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /plates/{plateDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `externalReferences`, `plateBarcode`, `plateDbId`, `plateFormat`, `plateName`, `programDbId`, `sampleType`, `studyDbId`, `trialDbId`

        Removed required properties:
        - `plateDbId`
        - `plateName`

##### `GET` /programs


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /programs


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /programs/{programDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `abbreviation`, `additionalInfo`, `commonCropName`, `documentationURL`, `externalReferences`, `fundingInformation`, `leadPersonDbId`, `leadPersonName`, `objective`, `programDbId`, `programName`, `programType`

        Removed required properties:
        - `programDbId`
        - `programName`

##### `PUT` /programs/{programDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `abbreviation`, `additionalInfo`, `commonCropName`, `documentationURL`, `externalReferences`, `fundingInformation`, `leadPersonDbId`, `leadPersonName`, `objective`, `programDbId`, `programName`, `programType`

        Removed required properties:
        - `programDbId`
        - `programName`

##### `GET` /references


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /references/{referenceDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        * Changed property `species`

            New properties: `term`, `termURI`

##### `GET` /references/{referenceDbId}/bases


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /referencesets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /referencesets/{referenceSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `assemblyPUI`, `commonCropName`, `externalReferences`, `isDerived`, `md5checksum`, `referenceSetDbId`, `referenceSetName`, `sourceAccessions`, `sourceGermplasm`, `sourceURI`, `species`

        Removed required properties:
        - `referenceSetDbId`
        - `referenceSetName`

##### `GET` /samples


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /samples


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /samples


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /samples/{sampleDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `column`, `externalReferences`, `germplasmDbId`, `observationUnitDbId`, `plateDbId`, `plateName`, `programDbId`, `row`, `sampleBarcode`, `sampleDescription`, `sampleGroupDbId`, `sampleName`, `samplePUI`, `sampleTimestamp`, `sampleType`, `studyDbId`, `takenBy`, `tissueType`, `trialDbId`, `well`

        Removed required properties:
        - `sampleName`

##### `GET` /scales


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /scales


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /scales/{scaleDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `dataType`, `decimalPlaces`, `externalReferences`, `ontologyReference`, `scaleDbId`, `scaleName`, `scalePUI`, `units`, `validValues`

        Removed required properties:
        - `scaleDbId`
        - `scaleName`

##### `PUT` /scales/{scaleDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `additionalInfo`, `dataType`, `decimalPlaces`, `externalReferences`, `ontologyReference`, `scaleName`, `scalePUI`, `units`, `validValues`

    New required properties:
    - `scaleName`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `dataType`, `decimalPlaces`, `externalReferences`, `ontologyReference`, `scaleDbId`, `scaleName`, `scalePUI`, `units`, `validValues`

        Removed required properties:
        - `scaleDbId`
        - `scaleName`

##### `POST` /search/allelematrix


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/allelematrix/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/attributes


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/attributes/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/attributevalues


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/attributevalues/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/calls/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/callsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/callsets/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/germplasm


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/germplasm/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/images/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/lists


###### Request:

* Changed content type : `application/json`

    * Changed property `listType`:
      - Removed enum values: [germplasm, markers, variants, programs, trials, studies, observationUnits, observations, observationVariables, samples]

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/lists/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/locations


###### Request:

* Changed content type : `application/json`

    * Changed property `coordinates`

        Deleted properties: `geometry`, `type`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/locations/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/markerpositions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/markerpositions/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/observations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/observations/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/observationunits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/observationunits/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/pedigree


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/pedigree/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/people


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/people/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/plates


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/plates/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/programs


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/programs/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/references


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/references/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/referencesets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/referencesets/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/samples


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/samples/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/studies


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/studies/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/trials


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/trials/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/variables


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/variables/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/variants


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/variants/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /search/variantsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /search/variantsets/{searchResultsDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /seasons


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /seasons


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /seasons/{seasonDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /seasons/{seasonDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /seedlots


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /seedlots


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /seedlots/transactions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /seedlots/transactions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /seedlots/{seedLotDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `amount`, `contentMixture`, `createdDate`, `externalReferences`, `lastUpdated`, `locationDbId`, `locationName`, `programDbId`, `programName`, `seedLotDbId`, `seedLotDescription`, `seedLotName`, `sourceCollection`, `storageLocation`, `units`

        Removed required properties:
        - `seedLotDbId`
        - `seedLotName`

##### `PUT` /seedlots/{seedLotDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `amount`, `contentMixture`, `createdDate`, `externalReferences`, `lastUpdated`, `locationDbId`, `locationName`, `programDbId`, `programName`, `seedLotDbId`, `seedLotDescription`, `seedLotName`, `sourceCollection`, `storageLocation`, `units`

        Removed required properties:
        - `seedLotDbId`
        - `seedLotName`

##### `GET` /seedlots/{seedLotDbId}/transactions


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /serverinfo


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /studies


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /studies


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /studytypes


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /traits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /traits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /traits/{traitDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `alternativeAbbreviations`, `attribute`, `attributePUI`, `entity`, `entityPUI`, `externalReferences`, `mainAbbreviation`, `ontologyReference`, `status`, `synonyms`, `traitClass`, `traitDbId`, `traitDescription`, `traitName`, `traitPUI`

        Removed required properties:
        - `traitDbId`
        - `traitName`

##### `PUT` /traits/{traitDbId}


###### Request:

* Changed content type : `application/json`

    New properties: `additionalInfo`, `alternativeAbbreviations`, `attribute`, `attributePUI`, `entity`, `entityPUI`, `externalReferences`, `mainAbbreviation`, `ontologyReference`, `status`, `synonyms`, `traitClass`, `traitDescription`, `traitName`, `traitPUI`

    New required properties:
    - `traitName`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `alternativeAbbreviations`, `attribute`, `attributePUI`, `entity`, `entityPUI`, `externalReferences`, `mainAbbreviation`, `ontologyReference`, `status`, `synonyms`, `traitClass`, `traitDbId`, `traitDescription`, `traitName`, `traitPUI`

        Removed required properties:
        - `traitDbId`
        - `traitName`

##### `GET` /trials


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /trials


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /trials/{trialDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `active`, `additionalInfo`, `commonCropName`, `contacts`, `datasetAuthorships`, `documentationURL`, `endDate`, `externalReferences`, `programDbId`, `programName`, `publications`, `startDate`, `trialDbId`, `trialDescription`, `trialName`, `trialPUI`

        Removed required properties:
        - `trialDbId`
        - `trialName`

##### `PUT` /trials/{trialDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `active`, `additionalInfo`, `commonCropName`, `contacts`, `datasetAuthorships`, `documentationURL`, `endDate`, `externalReferences`, `programDbId`, `programName`, `publications`, `startDate`, `trialDbId`, `trialDescription`, `trialName`, `trialPUI`

        Removed required properties:
        - `trialDbId`
        - `trialName`

##### `GET` /variables


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /variables


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variants


###### Parameters:

Added: `null` in `null`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variants/{variantDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variants/{variantDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variantsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /variantsets/extract


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variantsets/{variantSetDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variantsets/{variantSetDbId}/calls


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variantsets/{variantSetDbId}/callsets


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /variantsets/{variantSetDbId}/variants


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /attributes/{attributeDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `attributeCategory`, `attributeDbId`, `attributeDescription`, `attributeName`, `attributePUI`, `commonCropName`, `contextOfUse`, `defaultValue`, `documentationURL`, `externalReferences`, `growthStage`, `institution`, `language`, `method`, `ontologyReference`, `scale`, `scientist`, `status`, `submissionTimestamp`, `synonyms`, `trait`

        Removed required properties:
        - `attributeDbId`
        - `attributeName`
        - `method`
        - `scale`
        - `trait`

##### `PUT` /attributes/{attributeDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference`

        Deleted properties: `documentationLinks`, `ontologyDbId`, `ontologyName`, `version`

        Removed required properties:
        - `ontologyDbId`
        - `ontologyName`

    * Changed property `method`

        Deleted properties: `additionalInfo`, `bibliographicalReference`, `externalReferences`, `formula`, `methodClass`, `methodDbId`, `methodName`, `methodPUI`, `ontologyReference`

        Removed required properties:
        - `methodName`

    * Changed property `scale`

        Deleted properties: `additionalInfo`, `dataType`, `decimalPlaces`, `externalReferences`, `ontologyReference`, `scaleDbId`, `scaleName`, `scalePUI`, `units`, `validValues`

        Removed required properties:
        - `scaleDbId`
        - `scaleName`

    * Changed property `trait`

        Deleted properties: `additionalInfo`, `alternativeAbbreviations`, `attribute`, `attributePUI`, `entity`, `entityPUI`, `externalReferences`, `mainAbbreviation`, `ontologyReference`, `status`, `synonyms`, `traitClass`, `traitDbId`, `traitDescription`, `traitName`, `traitPUI`

        Removed required properties:
        - `traitName`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `attributeCategory`, `attributeDbId`, `attributeDescription`, `attributeName`, `attributePUI`, `commonCropName`, `contextOfUse`, `defaultValue`, `documentationURL`, `externalReferences`, `growthStage`, `institution`, `language`, `method`, `ontologyReference`, `scale`, `scientist`, `status`, `submissionTimestamp`, `synonyms`, `trait`

        Removed required properties:
        - `attributeDbId`
        - `attributeName`
        - `method`
        - `scale`
        - `trait`

##### `GET` /crosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /crosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /crosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /germplasm/{germplasmDbId}/mcpd


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /plannedcrosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /plannedcrosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /plannedcrosses


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /studies/{studyDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `active`, `additionalInfo`, `commonCropName`, `contacts`, `culturalPractices`, `dataLinks`, `documentationURL`, `endDate`, `environmentParameters`, `experimentalDesign`, `externalReferences`, `growthFacility`, `lastUpdate`, `license`, `locationDbId`, `locationName`, `observationLevels`, `observationUnitsDescription`, `observationVariableDbIds`, `seasons`, `startDate`, `studyCode`, `studyDbId`, `studyDescription`, `studyName`, `studyPUI`, `studyType`, `trialDbId`, `trialName`

        Removed required properties:
        - `studyDbId`
        - `studyName`

##### `PUT` /studies/{studyDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `active`, `additionalInfo`, `commonCropName`, `contacts`, `culturalPractices`, `dataLinks`, `documentationURL`, `endDate`, `environmentParameters`, `experimentalDesign`, `externalReferences`, `growthFacility`, `lastUpdate`, `license`, `locationDbId`, `locationName`, `observationLevels`, `observationUnitsDescription`, `observationVariableDbIds`, `seasons`, `startDate`, `studyCode`, `studyDbId`, `studyDescription`, `studyName`, `studyPUI`, `studyType`, `trialDbId`, `trialName`

        Removed required properties:
        - `studyDbId`
        - `studyName`

##### `GET` /variables/{observationVariableDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `commonCropName`, `contextOfUse`, `defaultValue`, `documentationURL`, `externalReferences`, `growthStage`, `institution`, `language`, `method`, `observationVariableDbId`, `observationVariableName`, `observationVariablePUI`, `ontologyReference`, `scale`, `scientist`, `status`, `submissionTimestamp`, `synonyms`, `trait`

        Removed required properties:
        - `method`
        - `observationVariableDbId`
        - `observationVariableName`
        - `scale`
        - `trait`

##### `PUT` /variables/{observationVariableDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `ontologyReference`

        Deleted properties: `documentationLinks`, `ontologyDbId`, `ontologyName`, `version`

        Removed required properties:
        - `ontologyDbId`
        - `ontologyName`

    * Changed property `method`

        Deleted properties: `additionalInfo`, `bibliographicalReference`, `externalReferences`, `formula`, `methodClass`, `methodDbId`, `methodName`, `methodPUI`, `ontologyReference`

        Removed required properties:
        - `methodName`

    * Changed property `scale`

        Deleted properties: `additionalInfo`, `dataType`, `decimalPlaces`, `externalReferences`, `ontologyReference`, `scaleDbId`, `scaleName`, `scalePUI`, `units`, `validValues`

        Removed required properties:
        - `scaleDbId`
        - `scaleName`

    * Changed property `trait`

        Deleted properties: `additionalInfo`, `alternativeAbbreviations`, `attribute`, `attributePUI`, `entity`, `entityPUI`, `externalReferences`, `mainAbbreviation`, `ontologyReference`, `status`, `synonyms`, `traitClass`, `traitDbId`, `traitDescription`, `traitName`, `traitPUI`

        Removed required properties:
        - `traitName`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `commonCropName`, `contextOfUse`, `defaultValue`, `documentationURL`, `externalReferences`, `growthStage`, `institution`, `language`, `method`, `observationVariableDbId`, `observationVariableName`, `observationVariablePUI`, `ontologyReference`, `scale`, `scientist`, `status`, `submissionTimestamp`, `synonyms`, `trait`

        Removed required properties:
        - `method`
        - `observationVariableDbId`
        - `observationVariableName`
        - `scale`
        - `trait`

##### `POST` /delete/images


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /images/{imageDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `copyright`, `descriptiveOntologyTerms`, `externalReferences`, `imageDbId`, `imageFileName`, `imageFileSize`, `imageHeight`, `imageLocation`, `imageName`, `imageTimeStamp`, `imageURL`, `imageWidth`, `mimeType`, `observationDbIds`, `observationUnitDbId`

        Removed required properties:
        - `imageDbId`

##### `PUT` /images/{imageDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `copyright`, `descriptiveOntologyTerms`, `externalReferences`, `imageDbId`, `imageFileName`, `imageFileSize`, `imageHeight`, `imageLocation`, `imageName`, `imageTimeStamp`, `imageURL`, `imageWidth`, `mimeType`, `observationDbIds`, `observationUnitDbId`

        Removed required properties:
        - `imageDbId`

##### `GET` /locations/{locationDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `abbreviation`, `additionalInfo`, `coordinateDescription`, `coordinateUncertainty`, `coordinates`, `countryCode`, `countryName`, `documentationURL`, `environmentType`, `exposure`, `externalReferences`, `instituteAddress`, `instituteName`, `locationDbId`, `locationName`, `locationType`, `parentLocationDbId`, `parentLocationName`, `siteStatus`, `slope`, `topography`

        Removed required properties:
        - `locationDbId`
        - `locationName`

##### `PUT` /locations/{locationDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `abbreviation`, `additionalInfo`, `coordinateDescription`, `coordinateUncertainty`, `coordinates`, `countryCode`, `countryName`, `documentationURL`, `environmentType`, `exposure`, `externalReferences`, `instituteAddress`, `instituteName`, `locationDbId`, `locationName`, `locationType`, `parentLocationDbId`, `parentLocationName`, `siteStatus`, `slope`, `topography`

        Removed required properties:
        - `locationDbId`
        - `locationName`

##### `GET` /observations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /observations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /observations


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /observations/{observationDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `collector`, `externalReferences`, `geoCoordinates`, `germplasmDbId`, `germplasmName`, `observationDbId`, `observationTimeStamp`, `observationUnitDbId`, `observationUnitName`, `observationVariableDbId`, `observationVariableName`, `season`, `studyDbId`, `uploadedBy`, `value`

        Removed required properties:
        - `observationDbId`

##### `PUT` /observations/{observationDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `season`

        Deleted properties: `season`, `seasonDbId`, `seasonName`, `year`

        Removed required properties:
        - `seasonDbId`

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `collector`, `externalReferences`, `geoCoordinates`, `germplasmDbId`, `germplasmName`, `observationDbId`, `observationTimeStamp`, `observationUnitDbId`, `observationUnitName`, `observationVariableDbId`, `observationVariableName`, `season`, `studyDbId`, `uploadedBy`, `value`

        Removed required properties:
        - `observationDbId`

##### `POST` /search/images


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

Changed response : **202**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /observationunits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `POST` /observationunits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `PUT` /observationunits


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

##### `GET` /observationunits/{observationUnitDbId}


###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `crossDbId`, `crossName`, `externalReferences`, `germplasmDbId`, `germplasmName`, `locationDbId`, `locationName`, `observationUnitDbId`, `observationUnitName`, `observationUnitPUI`, `observationUnitPosition`, `observations`, `programDbId`, `programName`, `seedLotDbId`, `seedLotName`, `studyDbId`, `studyName`, `treatments`, `trialDbId`, `trialName`

        Removed required properties:
        - `observationUnitDbId`

##### `PUT` /observationunits/{observationUnitDbId}


###### Request:

* Changed content type : `application/json`

    * Changed property `observationUnitPosition`

        * Changed property `positionCoordinateXType`:
          - Removed enum values: [LONGITUDE, LATITUDE, PLANTED_ROW, PLANTED_INDIVIDUAL, GRID_ROW, GRID_COL, MEASURED_ROW, MEASURED_COL]

        * Changed property `positionCoordinateYType`:
          - Removed enum values: [LONGITUDE, LATITUDE, PLANTED_ROW, PLANTED_INDIVIDUAL, GRID_ROW, GRID_COL, MEASURED_ROW, MEASURED_COL]

###### Return Type:

Changed response : **200**

* Changed content type : `application/json`

    * Changed property `metadata`

        Deleted properties: `datafiles`, `pagination`, `status`

    * Changed property `result`

        Deleted properties: `additionalInfo`, `crossDbId`, `crossName`, `externalReferences`, `germplasmDbId`, `germplasmName`, `locationDbId`, `locationName`, `observationUnitDbId`, `observationUnitName`, `observationUnitPUI`, `observationUnitPosition`, `observations`, `programDbId`, `programName`, `seedLotDbId`, `seedLotName`, `studyDbId`, `studyName`, `treatments`, `trialDbId`, `trialName`

        Removed required properties:
        - `observationUnitDbId`

