#### What's Deleted
---

##### `GET` /allelematrix

> Use this endpoint to retrieve a two dimensional matrix of genotype data


##### `GET` /attributes/categories

> Get the Categories of Germplasm Attributes


##### `GET` /commoncropnames

> Get the Common Crop Names


##### `POST` /delete/images

> Submit a delete request for `Images`


##### `POST` /delete/observations

> Submit a delete request for `Observations`


##### `GET` /germplasm/{germplasmDbId}/mcpd

> Get the details of a specific Germplasm in MCPD format


##### `GET` /germplasm/{germplasmDbId}/pedigree

> **Deprecated in v2.1** Please use `GET /pedigree?germplasmDbId={germplasmDbId}`. Github issue number #481 
> <br/> Get the pedigree details of a specific Germplasm


##### `GET` /germplasm/{germplasmDbId}/progeny

> **Deprecated in v2.1** Please use `GET /pedigree?germplasmDbId={germplasmDbId}`. Github issue number #481 
> <br/> Get the progeny details of a specific Germplasm


##### `PUT` /images/{imageDbId}/imagecontent

> Attach an image binary file to an existing image metadata record


##### `POST` /lists/{listDbId}/data

> Add new data members to a specific List


##### `POST` /lists/{listDbId}/items

> Add Items to a specific List


##### `GET` /maps/{mapDbId}/linkagegroups

> Get the Linkage Groups of a specific Genomic Map


##### `GET` /observationlevels

> Get the Observation Levels


##### `GET` /observations/table

> Get a list of Observations in a table format


##### `GET` /observationunits/table

> Get a list of Observations in a table format


##### `GET` /references/{referenceDbId}/bases

> Lists `Reference` bases by ID and optional range.


##### `GET` /seedlots/transactions

> Get a filtered list of Seed Lot Transactions


##### `POST` /seedlots/transactions

> Add new Seed Lot Transaction to be recorded


##### `GET` /seedlots/{seedLotDbId}/transactions

> Get all Transactions related to a specific Seed Lot


##### `GET` /serverinfo

> Get the list of implemented Calls


##### `GET` /studytypes

> Get the Study Types


##### `POST` /variantsets/extract

> Create new `VariantSet` based on search results


##### `GET` /vendor/orders

> List current available orders


##### `POST` /vendor/orders

> Submit New Order


##### `GET` /vendor/orders/{orderId}/plates

> Get the Plates for a specific Order


##### `GET` /vendor/orders/{orderId}/results

> Get the results of a specific Order


##### `GET` /vendor/orders/{orderId}/status

> Get the status of a specific Order


##### `POST` /vendor/plates

> Submit a new set of Sample data


##### `GET` /vendor/plates/{submissionId}

> Get the data for a submitted set of plates


##### `GET` /vendor/specifications

> Get the Vendor Specifications


##### `PUT` /calls

> Update existing `Calls` with new genotype value or metadata


##### `PUT` /observationunits/{observationUnitDbId}

> Update an existing Observation Units


##### `PUT` /pedigree

> Send a list of pedigree nodes to update existing information on a server


##### `PUT` /plates

> Update the details of existing Plates


##### `PUT` /samples/{sampleDbId}

> Update the details of an existing Sample


##### `PUT` /observations/{observationDbId}

> Update an existing Observation


#### What's Changed
---

##### `GET` /attributes

> Get a filtered list of GermplasmAttribute


###### Parameters:

Changed: `attributeCategory` in `query`
> General category for the attribute. very similar to Trait class.


Changed: `attributeDbId` in `query`
> List of Germplasm Attribute IDs to search for


Changed: `attributeName` in `query`
> List of human readable Germplasm Attribute names to search for


Changed: `methodDbId` in `query`
> List of methods to filter search results


Changed: `scaleDbId` in `query`
> The unique identifier for a Scale


Changed: `scaleName` in `query`
> Name of the scale
> <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable


Changed: `traitDbId` in `query`
> The unique identifier for a Trait


Changed: `traitName` in `query`
> The human readable name of a trait
> <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `attributeValueDbIds` (array)

                Items (string):

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `attributeDbId` (string)
                > The ID which uniquely identifies this attribute within the given database server


            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeCategory` (string)

            * Changed property `attributeDescription` (string)

            * Changed property `attributeName` (string)

            * Changed property `attributePUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `POST` /attributes

> Create new GermplasmAttribute


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `attributeValueDbIds` (array)

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `attributeDbId` (string)
                > The ID which uniquely identifies this attribute within the given database server


            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeCategory` (string)

            * Changed property `attributeDescription` (string)

            * Changed property `attributeName` (string)

            * Changed property `attributePUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `GET` /attributes/{attributeDbId}

> Get the details of a specific GermplasmAttribute


###### Parameters:

Deleted: `attributeDbId` in `path`
> The unique id for an attribute


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        New optional properties:
        - `method`
        - `scale`
        - `trait`

        * Added property `attributeValueDbIds` (array)

        * Added property `methodDbId` (string)

        * Added property `methodName` (string)

        * Added property `methodPUI` (string)

        * Added property `ontologyReferenceDbId` (string)

        * Added property `scaleDbId` (string)

        * Added property `scaleName` (string)

        * Added property `scalePUI` (string)

        * Added property `traitDbId` (string)

        * Added property `traitName` (string)

        * Added property `traitPUI` (string)

        * Deleted property `attributeDbId` (string)
            > The ID which uniquely identifies this attribute within the given database server


        * Deleted property `contextOfUse` (array)
            > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `method` (object)

        * Deleted property `ontologyReference` (object)

        * Deleted property `scale` (object)

        * Deleted property `synonyms` (array)
            > Other variable names


        * Deleted property `trait` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attributeCategory` (string)

        * Changed property `attributeDescription` (string)

        * Changed property `attributeName` (string)

        * Changed property `attributePUI` (string)

        * Changed property `commonCropName` (string)

        * Changed property `defaultValue` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `growthStage` (string)

        * Changed property `institution` (string)

        * Changed property `language` (string)

        * Changed property `scientist` (string)

        * Changed property `status` (string)

        * Changed property `submissionTimestamp` (string -> string)

##### `PUT` /attributes/{attributeDbId}

> Update the details for an existing GermplasmAttribute


###### Parameters:

Deleted: `attributeDbId` in `path`
> The unique id for an attribute


###### Request:

Changed content type : `application/json`

New required properties:
- `attributeDbId`
- `methodName`
- `scaleDbId`
- `scaleName`
- `traitName`

New optional properties:
- `method`
- `scale`
- `trait`

* Added property `attributeDbId` (string)

* Added property `attributeValueDbIds` (array)

* Added property `methodDbId` (string)

* Added property `methodName` (string)

* Added property `methodPUI` (string)

* Added property `ontologyReferenceDbId` (string)

* Added property `scaleDbId` (string)

* Added property `scaleName` (string)

* Added property `scalePUI` (string)

* Added property `traitDbId` (string)

* Added property `traitName` (string)

* Added property `traitPUI` (string)

* Deleted property `contextOfUse` (array)
    > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `method` (object)

* Deleted property `ontologyReference` (object)

* Deleted property `scale` (object)

* Deleted property `synonyms` (array)
    > Other variable names


* Deleted property `trait` (object)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `attributeCategory` (string)

* Changed property `attributeDescription` (string)

* Changed property `attributeName` (string)

* Changed property `attributePUI` (string)

* Changed property `commonCropName` (string)

* Changed property `defaultValue` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `growthStage` (string)

* Changed property `institution` (string)

* Changed property `language` (string)

* Changed property `scientist` (string)

* Changed property `status` (string)

* Changed property `submissionTimestamp` (string -> string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        New optional properties:
        - `method`
        - `scale`
        - `trait`

        * Added property `attributeValueDbIds` (array)

        * Added property `methodDbId` (string)

        * Added property `methodName` (string)

        * Added property `methodPUI` (string)

        * Added property `ontologyReferenceDbId` (string)

        * Added property `scaleDbId` (string)

        * Added property `scaleName` (string)

        * Added property `scalePUI` (string)

        * Added property `traitDbId` (string)

        * Added property `traitName` (string)

        * Added property `traitPUI` (string)

        * Deleted property `attributeDbId` (string)
            > The ID which uniquely identifies this attribute within the given database server


        * Deleted property `contextOfUse` (array)
            > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `method` (object)

        * Deleted property `ontologyReference` (object)

        * Deleted property `scale` (object)

        * Deleted property `synonyms` (array)
            > Other variable names


        * Deleted property `trait` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attributeCategory` (string)

        * Changed property `attributeDescription` (string)

        * Changed property `attributeName` (string)

        * Changed property `attributePUI` (string)

        * Changed property `commonCropName` (string)

        * Changed property `defaultValue` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `growthStage` (string)

        * Changed property `institution` (string)

        * Changed property `language` (string)

        * Changed property `scientist` (string)

        * Changed property `status` (string)

        * Changed property `submissionTimestamp` (string -> string)

##### `GET` /attributevalues

> Get a filtered list of GermplasmAttributeValue


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `ontologyDbId` in `query`
> List of ontology IDs to search for


Added: `methodDbId` in `query`
> List of methods to filter search results


Added: `scaleDbId` in `query`
> List of scales to filter search results


Added: `traitDbId` in `query`
> List of trait unique ID to filter search results


Added: `traitClass` in `query`
> List of trait classes to filter search results


Added: `dataType` in `query`
> List of scale data types to filter search results


Changed: `attributeValueDbId` in `query`
> List of Germplasm Attribute Value IDs to search for


Changed: `attributeDbId` in `query`
> List of Germplasm Attribute IDs to search for


Changed: `attributeName` in `query`
> List of human readable Germplasm Attribute names to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `attributePUI` (string)

            * Added property `germplasmPUI` (string)

            * Deleted property `attributeValueDbId` (string)
                > The ID which uniquely identifies this attribute value within the given database server


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeDbId` (string)

            * Changed property `attributeName` (string)

            * Changed property `determinedDate` (string -> string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `value` (string)

##### `POST` /attributevalues

> Create new GermplasmAttributeValue


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `attributePUI` (string)

            * Added property `germplasmPUI` (string)

            * Deleted property `attributeValueDbId` (string)
                > The ID which uniquely identifies this attribute value within the given database server


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeDbId` (string)

            * Changed property `attributeName` (string)

            * Changed property `determinedDate` (string -> string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `value` (string)

##### `GET` /attributevalues/{attributeValueDbId}

> Get the details of a specific GermplasmAttributeValue


###### Parameters:

Deleted: `attributeValueDbId` in `path`
> The unique id for an attribute value


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `attributePUI` (string)

        * Added property `germplasmPUI` (string)

        * Deleted property `attributeValueDbId` (string)
            > The ID which uniquely identifies this attribute value within the given database server


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attributeDbId` (string)

        * Changed property `attributeName` (string)

        * Changed property `determinedDate` (string -> string)

        * Changed property `germplasmDbId` (string)

        * Changed property `germplasmName` (string)

        * Changed property `value` (string)

##### `PUT` /attributevalues/{attributeValueDbId}

> Update the details for an existing GermplasmAttributeValue


###### Parameters:

Deleted: `attributeValueDbId` in `path`
> The unique id for an attribute value


###### Request:

Changed content type : `application/json`

New required properties:
- `attributeValueDbId`

* Added property `attributePUI` (string)

* Added property `attributeValueDbId` (string)

* Added property `germplasmPUI` (string)

* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `attributeDbId` (string)

* Changed property `attributeName` (string)

* Changed property `determinedDate` (string -> string)

* Changed property `germplasmDbId` (string)

* Changed property `germplasmName` (string)

* Changed property `value` (string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `attributePUI` (string)

        * Added property `germplasmPUI` (string)

        * Deleted property `attributeValueDbId` (string)
            > The ID which uniquely identifies this attribute value within the given database server


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attributeDbId` (string)

        * Changed property `attributeName` (string)

        * Changed property `determinedDate` (string -> string)

        * Changed property `germplasmDbId` (string)

        * Changed property `germplasmName` (string)

        * Changed property `value` (string)

##### `GET` /breedingmethods

> Get a filtered list of BreedingMethod


###### Parameters:

Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `abbreviation`
            - `breedingMethodName`
            - `description`

            * Changed property `abbreviation` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `description` (string)

##### `GET` /breedingmethods/{breedingMethodDbId}

> Get the details of a specific BreedingMethod


###### Parameters:

Deleted: `breedingMethodDbId` in `path`
> Internal database identifier for a breeding method


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `abbreviation`
        - `breedingMethodName`
        - `description`

        * Changed property `abbreviation` (string)

        * Changed property `breedingMethodDbId` (string)

        * Changed property `breedingMethodName` (string)

        * Changed property `description` (string)

##### `GET` /calls

> Get a filtered list of Call


###### Parameters:

Added: `expandHomozygote` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `expandHomozygotes` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Changed: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variant` within the given database server


Changed: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Changed: `unknownString` in `query`
> The string used as a representation for missing data.


Changed: `sepPhased` in `query`
> The string used as a separator for phased allele calls.


Changed: `sepUnphased` in `query`
> The string used as a separator for unphased allele calls.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /callsets

> Get a filtered list of CallSet


###### Parameters:

Added: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyDbId` in `query`
> List of study identifiers to search for


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `sampleName` in `query`
> A list of human readable names associated with `Samples`


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Changed: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Changed: `callSetName` in `query`
> A list of human readable names associated with `CallSets`


Changed: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Changed: `sampleDbId` in `query`
> A list of IDs which uniquely identify `Samples` within the given database server


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleName` (string)

            * Added property `samplePUI` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `created` (string -> string)

            * Changed property `sampleDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `updated` (string -> string)

            * Changed property `variantSetDbIds` (array)

##### `GET` /callsets/{callSetDbId}

> Get the details of a specific CallSet


###### Parameters:

Deleted: `callSetDbId` in `path`
> The ID which uniquely identifies a `CallSet` within the given database server


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `sampleName` (string)

        * Added property `samplePUI` (string)

        * Added property `studyName` (string)

        * Added property `studyPUI` (string)

        * Deleted property `externalReferences` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `callSetDbId` (string)

        * Changed property `callSetName` (string)

        * Changed property `created` (string -> string)

        * Changed property `sampleDbId` (string)

        * Changed property `studyDbId` (string)

        * Changed property `updated` (string -> string)

        * Changed property `variantSetDbIds` (array)

##### `GET` /callsets/{callSetDbId}/calls

> Get a filtered list of Call


###### Parameters:

Added: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Added: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variant` within the given database server


Added: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Added: `expandHomozygote` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `callSetDbId` in `path`
> The ID which uniquely identifies a `CallSet` within the given database server


Deleted: `expandHomozygotes` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `unknownString` in `query`
> The string used as a representation for missing data.


Changed: `sepPhased` in `query`
> The string used as a separator for phased allele calls.


Changed: `sepUnphased` in `query`
> The string used as a separator for unphased allele calls.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /crossingprojects

> Get a filtered list of CrossingProject


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `includePotentialParent` in `query`
> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


Deleted: `includePotentialParents` in `query`
> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `crossingProjectDbId` (string)
                > The unique identifier for a crossing project


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `potentialParents` (array)
                > A list of all the potential parents in the crossing block, available in the crossing project
                > <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `crossingProjectDescription` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

##### `POST` /crossingprojects

> Create new CrossingProject


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `crossingProjectDbId` (string)
                > The unique identifier for a crossing project


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `potentialParents` (array)
                > A list of all the potential parents in the crossing block, available in the crossing project
                > <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `crossingProjectDescription` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

##### `GET` /crossingprojects/{crossingProjectDbId}

> Get the details of a specific CrossingProject


###### Parameters:

Deleted: `crossingProjectDbId` in `path`
> The unique identifier for a crossing project


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `crossingProjectDbId` (string)
            > The unique identifier for a crossing project


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `potentialParents` (array)
            > A list of all the potential parents in the crossing block, available in the crossing project
            > <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `crossingProjectDescription` (string)

        * Changed property `crossingProjectName` (string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

##### `PUT` /crossingprojects/{crossingProjectDbId}

> Update the details for an existing CrossingProject


###### Parameters:

Deleted: `crossingProjectDbId` in `path`
> Search for Crossing Projects with this unique id


###### Request:

Changed content type : `application/json`

New required properties:
- `crossingProjectDbId`
- `crossingProjectDbId`

* Added property `crossingProjectDbId` (string)

* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `potentialParents` (array)
    > A list of all the potential parents in the crossing block, available in the crossing project
    > <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `commonCropName` (string)

* Changed property `crossingProjectDescription` (string)

* Changed property `crossingProjectName` (string)

* Changed property `programDbId` (string)

* Changed property `programName` (string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `crossingProjectDbId` (string)
            > The unique identifier for a crossing project


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `potentialParents` (array)
            > A list of all the potential parents in the crossing block, available in the crossing project
            > <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `crossingProjectDescription` (string)

        * Changed property `crossingProjectName` (string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

##### `GET` /events

> Get a filtered list of Event


###### Parameters:

Added: `studyName` in `query`
> List of study names to filter search results


Changed: `observationUnitDbId` in `query`
> The ID which uniquely identifies an observation unit.


Changed: `eventDbId` in `query`
> Filter based on an Event DbId.


Changed: `dateRangeStart` in `query`
> Filter based on an Event start date.


Changed: `dateRangeEnd` in `query`
> Filter based on an Event start date.


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `studyPUI` (string)

            * Deleted property `date` (array)
                > **Deprecated in v2.1** Please use `eventDateRange.discreteDates`. Github issue number #440             
                > <br>A list of dates when the event occurred
                > <br>MIAPPE V1.1 (DM-68) Event date - Date and time of the event.


            * Deleted property `eventDateRange` (object)

            * Deleted property `eventParameters` (array)
                > A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `eventDbId` (string)

            * Changed property `eventDescription` (string)

            * Changed property `eventType` (string)

            * Changed property `eventTypeDbId` (string)

            * Changed property `observationUnitDbIds` (array)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

##### `GET` /germplasm


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `familyCode` in `query`
> A familyCode representing the family this germplasm belongs to.


Added: `instituteCode` in `query`
> The code for the institute that maintains the material. 
> <br/> MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".


Added: `genu` in `query`
> List of Genus names to identify germplasm


Added: `specy` in `query`
> List of Species names to identify germplasm


Deleted: `genus` in `query`
> Genus name to identify germplasm


Deleted: `species` in `query`
> Species name to identify germplasm


Changed: `accessionNumber` in `query`
> A collection of unique identifiers for materials or germplasm within a genebank
> 
> MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").


Changed: `binomialName` in `query`
> List of the full binomial name (scientific name) to identify a germplasm


Changed: `synonym` in `query`
> List of alternative names or IDs used to reference this germplasm


Changed: `parentDbId` in `query`
> Search for Germplasm with these parents


Changed: `progenyDbId` in `query`
> Search for Germplasm with these children


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Changed: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Changed: `germplasmPUI` in `query`
> List of Permanent Unique Identifiers to identify germplasm


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleDbIds` (array)

            * Deleted property `donors` (array)
                > List of donor institutes


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `germplasmDbId` (string)
                > The ID which uniquely identifies a germplasm within the given database server 
                > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


            * Deleted property `germplasmOrigin` (array)
                > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


            * Deleted property `storageTypes` (array)
                > The type of storage this germplasm is kept in at a genebank.


            * Deleted property `synonyms` (array)
                > List of alternative names or IDs used to reference this germplasm
                > 
                > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


            * Deleted property `taxonIds` (array)
                > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
                > 
                > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


            * Changed property `accessionNumber` (string)

            * Changed property `acquisitionDate` (string -> string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `biologicalStatusOfAccessionCode` (string)
                > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
                > 
                > 100) Wild 
                > 110) Natural 
                > 120) Semi-natural/wild 
                > 130) Semi-natural/sown 
                > 200) Weedy 
                > 300) Traditional cultivar/landrace 
                > 400) Breeding/research material 
                > 410) Breeders line 
                > 411) Synthetic population 
                > 412) Hybrid 
                > 413) Founder stock/base population 
                > 414) Inbred line (parent of hybrid cultivar) 
                > 415) Segregating population 
                > 416) Clonal selection 
                > 420) Genetic stock 
                > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
                > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
                > 423) Other genetic stocks (e.g. mapping populations) 
                > 500) Advanced or improved cultivar (conventional breeding methods) 
                > 600) GMO (by genetic engineering) 
                > 999) Other (Elaborate in REMARKS field)


            * Changed property `biologicalStatusOfAccessionDescription` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `collection` (string)

            * Changed property `commonCropName` (string)

            * Changed property `countryOfOriginCode` (string)

            * Changed property `defaultDisplayName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `genus` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `germplasmPreprocessing` (string)

            * Changed property `instituteCode` (string)

            * Changed property `instituteName` (string)

            * Changed property `pedigree` (string)

            * Changed property `seedSource` (string)

            * Changed property `seedSourceDescription` (string)

            * Changed property `species` (string)

            * Changed property `speciesAuthority` (string)

            * Changed property `subtaxa` (string)

            * Changed property `subtaxaAuthority` (string)

##### `POST` /germplasm

> Create new Germplasm


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleDbIds` (array)

            * Deleted property `donors` (array)
                > List of donor institutes


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `germplasmDbId` (string)
                > The ID which uniquely identifies a germplasm within the given database server 
                > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


            * Deleted property `germplasmOrigin` (array)
                > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


            * Deleted property `storageTypes` (array)
                > The type of storage this germplasm is kept in at a genebank.


            * Deleted property `synonyms` (array)
                > List of alternative names or IDs used to reference this germplasm
                > 
                > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


            * Deleted property `taxonIds` (array)
                > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
                > 
                > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


            * Changed property `accessionNumber` (string)

            * Changed property `acquisitionDate` (string -> string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `biologicalStatusOfAccessionCode` (string)
                > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
                > 
                > 100) Wild 
                > 110) Natural 
                > 120) Semi-natural/wild 
                > 130) Semi-natural/sown 
                > 200) Weedy 
                > 300) Traditional cultivar/landrace 
                > 400) Breeding/research material 
                > 410) Breeders line 
                > 411) Synthetic population 
                > 412) Hybrid 
                > 413) Founder stock/base population 
                > 414) Inbred line (parent of hybrid cultivar) 
                > 415) Segregating population 
                > 416) Clonal selection 
                > 420) Genetic stock 
                > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
                > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
                > 423) Other genetic stocks (e.g. mapping populations) 
                > 500) Advanced or improved cultivar (conventional breeding methods) 
                > 600) GMO (by genetic engineering) 
                > 999) Other (Elaborate in REMARKS field)


            * Changed property `biologicalStatusOfAccessionDescription` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `collection` (string)

            * Changed property `commonCropName` (string)

            * Changed property `countryOfOriginCode` (string)

            * Changed property `defaultDisplayName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `genus` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `germplasmPreprocessing` (string)

            * Changed property `instituteCode` (string)

            * Changed property `instituteName` (string)

            * Changed property `pedigree` (string)

            * Changed property `seedSource` (string)

            * Changed property `seedSourceDescription` (string)

            * Changed property `species` (string)

            * Changed property `speciesAuthority` (string)

            * Changed property `subtaxa` (string)

            * Changed property `subtaxaAuthority` (string)

##### `GET` /germplasm/{germplasmDbId}


###### Parameters:

Deleted: `germplasmDbId` in `path`
> The internal id of the germplasm


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `sampleDbIds` (array)

        * Deleted property `donors` (array)
            > List of donor institutes


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `germplasmDbId` (string)
            > The ID which uniquely identifies a germplasm within the given database server 
            > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


        * Deleted property `germplasmOrigin` (array)
            > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


        * Deleted property `storageTypes` (array)
            > The type of storage this germplasm is kept in at a genebank.


        * Deleted property `synonyms` (array)
            > List of alternative names or IDs used to reference this germplasm
            > 
            > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


        * Deleted property `taxonIds` (array)
            > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
            > 
            > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


        * Changed property `accessionNumber` (string)

        * Changed property `acquisitionDate` (string -> string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `biologicalStatusOfAccessionCode` (string)
            > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
            > 
            > 100) Wild 
            > 110) Natural 
            > 120) Semi-natural/wild 
            > 130) Semi-natural/sown 
            > 200) Weedy 
            > 300) Traditional cultivar/landrace 
            > 400) Breeding/research material 
            > 410) Breeders line 
            > 411) Synthetic population 
            > 412) Hybrid 
            > 413) Founder stock/base population 
            > 414) Inbred line (parent of hybrid cultivar) 
            > 415) Segregating population 
            > 416) Clonal selection 
            > 420) Genetic stock 
            > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
            > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
            > 423) Other genetic stocks (e.g. mapping populations) 
            > 500) Advanced or improved cultivar (conventional breeding methods) 
            > 600) GMO (by genetic engineering) 
            > 999) Other (Elaborate in REMARKS field)


        * Changed property `biologicalStatusOfAccessionDescription` (string)

        * Changed property `breedingMethodDbId` (string)

        * Changed property `breedingMethodName` (string)

        * Changed property `collection` (string)

        * Changed property `commonCropName` (string)

        * Changed property `countryOfOriginCode` (string)

        * Changed property `defaultDisplayName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `genus` (string)

        * Changed property `germplasmName` (string)

        * Changed property `germplasmPUI` (string)

        * Changed property `germplasmPreprocessing` (string)

        * Changed property `instituteCode` (string)

        * Changed property `instituteName` (string)

        * Changed property `pedigree` (string)

        * Changed property `seedSource` (string)

        * Changed property `seedSourceDescription` (string)

        * Changed property `species` (string)

        * Changed property `speciesAuthority` (string)

        * Changed property `subtaxa` (string)

        * Changed property `subtaxaAuthority` (string)

##### `PUT` /germplasm/{germplasmDbId}

> Update the details for an existing Germplasm


###### Parameters:

Deleted: `germplasmDbId` in `path`
> The internal id of the germplasm


###### Request:

Changed content type : `application/json`

New required properties:
- `germplasmDbId`
- `germplasmDbId`

* Added property `germplasmDbId` (string)

* Added property `sampleDbIds` (array)

* Deleted property `donors` (array)
    > List of donor institutes


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `germplasmOrigin` (array)
    > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


* Deleted property `storageTypes` (array)
    > The type of storage this germplasm is kept in at a genebank.


* Deleted property `synonyms` (array)
    > List of alternative names or IDs used to reference this germplasm
    > 
    > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


* Deleted property `taxonIds` (array)
    > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
    > 
    > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


* Changed property `accessionNumber` (string)

* Changed property `acquisitionDate` (string -> string)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `biologicalStatusOfAccessionCode` (string)
    > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
    > 
    > 100) Wild 
    > 110) Natural 
    > 120) Semi-natural/wild 
    > 130) Semi-natural/sown 
    > 200) Weedy 
    > 300) Traditional cultivar/landrace 
    > 400) Breeding/research material 
    > 410) Breeders line 
    > 411) Synthetic population 
    > 412) Hybrid 
    > 413) Founder stock/base population 
    > 414) Inbred line (parent of hybrid cultivar) 
    > 415) Segregating population 
    > 416) Clonal selection 
    > 420) Genetic stock 
    > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
    > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
    > 423) Other genetic stocks (e.g. mapping populations) 
    > 500) Advanced or improved cultivar (conventional breeding methods) 
    > 600) GMO (by genetic engineering) 
    > 999) Other (Elaborate in REMARKS field)


* Changed property `biologicalStatusOfAccessionDescription` (string)

* Changed property `breedingMethodDbId` (string)

* Changed property `breedingMethodName` (string)

* Changed property `collection` (string)

* Changed property `commonCropName` (string)

* Changed property `countryOfOriginCode` (string)

* Changed property `defaultDisplayName` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `genus` (string)

* Changed property `germplasmName` (string)

* Changed property `germplasmPUI` (string)

* Changed property `germplasmPreprocessing` (string)

* Changed property `instituteCode` (string)

* Changed property `instituteName` (string)

* Changed property `pedigree` (string)

* Changed property `seedSource` (string)

* Changed property `seedSourceDescription` (string)

* Changed property `species` (string)

* Changed property `speciesAuthority` (string)

* Changed property `subtaxa` (string)

* Changed property `subtaxaAuthority` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `sampleDbIds` (array)

        * Deleted property `donors` (array)
            > List of donor institutes


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `germplasmDbId` (string)
            > The ID which uniquely identifies a germplasm within the given database server 
            > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


        * Deleted property `germplasmOrigin` (array)
            > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


        * Deleted property `storageTypes` (array)
            > The type of storage this germplasm is kept in at a genebank.


        * Deleted property `synonyms` (array)
            > List of alternative names or IDs used to reference this germplasm
            > 
            > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


        * Deleted property `taxonIds` (array)
            > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
            > 
            > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


        * Changed property `accessionNumber` (string)

        * Changed property `acquisitionDate` (string -> string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `biologicalStatusOfAccessionCode` (string)
            > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
            > 
            > 100) Wild 
            > 110) Natural 
            > 120) Semi-natural/wild 
            > 130) Semi-natural/sown 
            > 200) Weedy 
            > 300) Traditional cultivar/landrace 
            > 400) Breeding/research material 
            > 410) Breeders line 
            > 411) Synthetic population 
            > 412) Hybrid 
            > 413) Founder stock/base population 
            > 414) Inbred line (parent of hybrid cultivar) 
            > 415) Segregating population 
            > 416) Clonal selection 
            > 420) Genetic stock 
            > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
            > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
            > 423) Other genetic stocks (e.g. mapping populations) 
            > 500) Advanced or improved cultivar (conventional breeding methods) 
            > 600) GMO (by genetic engineering) 
            > 999) Other (Elaborate in REMARKS field)


        * Changed property `biologicalStatusOfAccessionDescription` (string)

        * Changed property `breedingMethodDbId` (string)

        * Changed property `breedingMethodName` (string)

        * Changed property `collection` (string)

        * Changed property `commonCropName` (string)

        * Changed property `countryOfOriginCode` (string)

        * Changed property `defaultDisplayName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `genus` (string)

        * Changed property `germplasmName` (string)

        * Changed property `germplasmPUI` (string)

        * Changed property `germplasmPreprocessing` (string)

        * Changed property `instituteCode` (string)

        * Changed property `instituteName` (string)

        * Changed property `pedigree` (string)

        * Changed property `seedSource` (string)

        * Changed property `seedSourceDescription` (string)

        * Changed property `species` (string)

        * Changed property `speciesAuthority` (string)

        * Changed property `subtaxa` (string)

        * Changed property `subtaxaAuthority` (string)

##### `GET` /lists

> Get a filtered list of List


###### Parameters:

Added: `dateCreatedRangeStart` in `query`
> Define the beginning for an interval of time and only include Lists that are created within this interval.


Added: `dateCreatedRangeEnd` in `query`
> Define the end for an interval of time and only include Lists that are created within this interval.


Added: `dateModifiedRangeStart` in `query`
> Define the beginning for an interval of time and only include Lists that are modified within this interval.


Added: `dateModifiedRangeEnd` in `query`
> Define the end for an interval of time and only include Lists that are modified within this interval.


Added: `listOwnerName` in `query`
> An array of names for the people or entities who are responsible for a set of Lists


Added: `listOwnerPersonDbId` in `query`
> An array of primary database identifiers to identify people or entities who are responsible for a set of Lists


Deleted: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crop. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Deleted: `programDbId` in `query`
> Use this parameter to only return results associated with the given `Program` unique identifier. 
> <br/>Use `GET /programs` to find the list of available `Programs` on a server.


Changed: `listName` in `query`
> An array of human readable names to identify a set of Lists


Changed: `listDbId` in `query`
> An array of primary database identifiers to identify a set of Lists


Changed: `listSource` in `query`
> An array of terms identifying lists from different sources (ie 'USER', 'SYSTEM', etc)


Changed: `listType` in `query`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `listDbId` (string)
                > The unique identifier for a List


            * Deleted property `listOwnerPersonDbId` (string)
                > The unique identifier for a List Owner. (usually a user or person)


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dateCreated` (string -> string)

            * Changed property `dateModified` (string -> string)

            * Changed property `listDescription` (string)

            * Changed property `listName` (string)

            * Changed property `listOwnerName` (string)

            * Changed property `listSize` (integer -> integer)

            * Changed property `listSource` (string)

            * Changed property `listType` (string)
                > The type of objects that are referenced in a List


##### `POST` /lists

> Create new List


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `listDbId` (string)
                > The unique identifier for a List


            * Deleted property `listOwnerPersonDbId` (string)
                > The unique identifier for a List Owner. (usually a user or person)


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dateCreated` (string -> string)

            * Changed property `dateModified` (string -> string)

            * Changed property `listDescription` (string)

            * Changed property `listName` (string)

            * Changed property `listOwnerName` (string)

            * Changed property `listSize` (integer -> integer)

            * Changed property `listSource` (string)

            * Changed property `listType` (string)
                > The type of objects that are referenced in a List


##### `GET` /lists/{listDbId}


###### Parameters:

Deleted: `listDbId` in `path`
> The unique identifier of a List


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `personDbId` (string)

        * Deleted property `data` (array)
            > The array of DbIds of the BrAPI objects contained in a List


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `listDbId` (string)
            > The unique identifier for a List


        * Deleted property `listOwnerPersonDbId` (string)
            > The unique identifier for a List Owner. (usually a user or person)


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `dateCreated` (string -> string)

        * Changed property `dateModified` (string -> string)

        * Changed property `listDescription` (string)

        * Changed property `listName` (string)

        * Changed property `listOwnerName` (string)

        * Changed property `listSize` (integer -> integer)

        * Changed property `listSource` (string)

        * Changed property `listType` (string)
            > The type of objects that are referenced in a List


##### `PUT` /lists/{listDbId}

> Update the details for an existing List


###### Parameters:

Deleted: `listDbId` in `path`
> The unique identifier of a List


###### Request:

Changed content type : `application/json`

New required properties:
- `listDbId`
- `listDbId`

* Added property `listDbId` (string)

* Added property `personDbId` (string)

* Deleted property `data` (array)
    > The array of DbIds of the BrAPI objects contained in a List


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `listOwnerPersonDbId` (string)
    > The unique identifier for a List Owner. (usually a user or person)


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `dateCreated` (string -> string)

* Changed property `dateModified` (string -> string)

* Changed property `listDescription` (string)

* Changed property `listName` (string)

* Changed property `listOwnerName` (string)

* Changed property `listSize` (integer -> integer)

* Changed property `listSource` (string)

* Changed property `listType` (string)
    > The type of objects that are referenced in a List


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `personDbId` (string)

        * Deleted property `data` (array)
            > The array of DbIds of the BrAPI objects contained in a List


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `listDbId` (string)
            > The unique identifier for a List


        * Deleted property `listOwnerPersonDbId` (string)
            > The unique identifier for a List Owner. (usually a user or person)


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `dateCreated` (string -> string)

        * Changed property `dateModified` (string -> string)

        * Changed property `listDescription` (string)

        * Changed property `listName` (string)

        * Changed property `listOwnerName` (string)

        * Changed property `listSize` (integer -> integer)

        * Changed property `listSource` (string)

        * Changed property `listType` (string)
            > The type of objects that are referenced in a List


##### `GET` /maps

> Get a filtered list of GenomeMap


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New optional properties:
            - `mapName`

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `comments` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `linkageGroupCount` (integer -> integer)

            * Changed property `mapDbId` (string)

            * Changed property `mapName` (string)

            * Changed property `mapPUI` (string)

            * Changed property `markerCount` (integer -> integer)

            * Changed property `publishedDate` (string -> string)

            * Changed property `scientificName` (string)

            * Changed property `type` (string)

            * Changed property `unit` (string)

##### `GET` /maps/{mapDbId}

> Get the details of a specific GenomeMap


###### Parameters:

Deleted: `mapDbId` in `path`
> The ID which uniquely identifies a `GenomeMap`


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New optional properties:
        - `mapName`

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `comments` (string)

        * Changed property `commonCropName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `linkageGroupCount` (integer -> integer)

        * Changed property `mapDbId` (string)

        * Changed property `mapName` (string)

        * Changed property `mapPUI` (string)

        * Changed property `markerCount` (integer -> integer)

        * Changed property `publishedDate` (string -> string)

        * Changed property `scientificName` (string)

        * Changed property `type` (string)

        * Changed property `unit` (string)

##### `GET` /markerpositions

> Get a filtered list of MarkerPosition


###### Parameters:

Changed: `mapDbId` in `query`
> A list of IDs which uniquely identify `GenomeMaps` within the given database server


Changed: `linkageGroupName` in `query`
> A list of Uniquely Identifiable linkage group names


Changed: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variants` within the given database server


Changed: `minPosition` in `query`
> The minimum position of markers in a given map


Changed: `maxPosition` in `query`
> The maximum position of markers in a given map


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `mapPUI` (string)

            * Deleted property `variantName` (string)
                > The human readable name for a `Variant`
                > <br> A `Variant` can also represent a Marker


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `linkageGroupName` (string)

            * Changed property `mapDbId` (string)

            * Changed property `mapName` (string)

            * Changed property `position` (integer -> integer)

            * Changed property `variantDbId` (string)

##### `GET` /methods

> Get a filtered list of Method


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `scaleDbId` in `query`
> The unique identifier for a method.


Deleted: `methodDbId` in `query`
> The unique identifier for a method


Changed: `observationVariableDbId` in `query`
> The unique identifier for an observation variable.


Changed: `ontologyDbId` in `query`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
>   Use `GET /ontologies` to find the list of available ontologies on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `methodDbId` (string)
                > Method unique identifier


            * Deleted property `ontologyReference` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `bibliographicalReference` (string)

            * Changed property `description` (string)

            * Changed property `formula` (string)

            * Changed property `methodClass` (string)

            * Changed property `methodName` (string)

            * Changed property `methodPUI` (string)

##### `POST` /methods

> Create new Method


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `methodDbId` (string)
                > Method unique identifier


            * Deleted property `ontologyReference` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `bibliographicalReference` (string)

            * Changed property `description` (string)

            * Changed property `formula` (string)

            * Changed property `methodClass` (string)

            * Changed property `methodName` (string)

            * Changed property `methodPUI` (string)

##### `GET` /methods/{methodDbId}

> Get the details of a specific Method


###### Parameters:

Deleted: `methodDbId` in `path`
> Id of the method to retrieve details of.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `methodDbId` (string)
            > Method unique identifier


        * Deleted property `ontologyReference` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `bibliographicalReference` (string)

        * Changed property `description` (string)

        * Changed property `formula` (string)

        * Changed property `methodClass` (string)

        * Changed property `methodName` (string)

        * Changed property `methodPUI` (string)

##### `PUT` /methods/{methodDbId}

> Update the details for an existing Method


###### Parameters:

Deleted: `methodDbId` in `path`
> Id of the method to retrieve details of.


###### Request:

Changed content type : `application/json`

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `methodDbId` (string)
            > Method unique identifier


        * Deleted property `ontologyReference` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `bibliographicalReference` (string)

        * Changed property `description` (string)

        * Changed property `formula` (string)

        * Changed property `methodClass` (string)

        * Changed property `methodName` (string)

        * Changed property `methodPUI` (string)

##### `GET` /observationunits

> Get a filtered list of ObservationUnit


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `locationName` in `query`
> A human readable names to search for


Added: `studyName` in `query`
> List of study names to filter search results


Added: `observationVariableDbId` in `query`
> The DbIds of Variables to search for


Added: `observationVariableName` in `query`
> The names of Variables to search for


Added: `observationVariablePUI` in `query`
> The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `observationLevel` in `query`
> Searches for values in ObservationUnit->observationUnitPosition->observationLevel


Added: `observationLevelRelationship` in `query`
> Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships


Added: `includeObservation` in `query`
> Use this parameter to include a list of observations embedded in each ObservationUnit object. 
> 
> CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to.


Deleted: `includeObservations` in `query`
> Use this parameter to include a list of observations embedded in each ObservationUnit object. 
> 
> CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to.


Deleted: `observationUnitLevelName` in `query`
> The Observation Unit Level. Returns only the observation unit of the specified Level. 
> <br/>References ObservationUnit->observationUnitPosition->observationLevel->levelName 
> <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelOrder` in `query`
> The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. 
> References ObservationUnit->observationUnitPosition->observationLevel->levelOrder 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelCode` in `query`
> The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` 
> or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipName` in `query`
> The Observation Unit Level Relationship is a connection that this observation unit has to another level of the hierarchy. 
> <br/>For example, if you have several observation units at a 'plot' level, they might all share a relationship to the same 'field' level.  
> <br/>Use this parameter to identify groups of observation units that share a relationship level. 
> <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipOrder` in `query`
> The Observation Unit Level Order Number. 
> <br/>Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipCode` in `query`
> The Observation Unit Level Code. 
> <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipDbId` in `query`
> The observationUnitDbId associated with a particular level and code.
> <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->observationUnitDbId 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Changed: `observationUnitDbId` in `query`
> The unique id of an observation unit


Changed: `locationDbId` in `query`
> The location ids to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `studyPUI` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationUnitDbId` (string)
                > The ID which uniquely identifies an observation unit
                > 
                > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


            * Deleted property `observationUnitPosition` (object)

            * Deleted property `observations` (array)
                > All observations attached to this observation unit. 
                > 
                > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


            * Deleted property `treatments` (array)
                > List of treatments applied to an observation unit.
                > 
                > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossDbId` (string)

            * Changed property `crossName` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationUnitPUI` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDbId` (string)

            * Changed property `seedLotName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

##### `PUT` /observationunits

> Update the details for an existing ObservationUnit


###### Request:

Changed content type : `application/json`

New required properties:
- `observationUnitDbId`
- `observationUnitDbId`

* Added property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Property `additionalProperties` (string)

* Added property `crossDbId` (string)

* Added property `crossName` (string)

* Added property `germplasmDbId` (string)

* Added property `germplasmName` (string)

* Added property `germplasmPUI` (string)

* Added property `locationDbId` (string)

* Added property `locationName` (string)

* Added property `observationUnitDbId` (string)

* Added property `observationUnitName` (string)

* Added property `observationUnitPUI` (string)

* Added property `programDbId` (string)

* Added property `programName` (string)

* Added property `seedLotDbId` (string)

* Added property `seedLotName` (string)

* Added property `studyDbId` (string)

* Added property `studyName` (string)

* Added property `studyPUI` (string)

* Added property `trialDbId` (string)

* Added property `trialName` (string)

* Added property `trialPUI` (string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `studyPUI` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationUnitDbId` (string)
                > The ID which uniquely identifies an observation unit
                > 
                > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


            * Deleted property `observationUnitPosition` (object)

            * Deleted property `observations` (array)
                > All observations attached to this observation unit. 
                > 
                > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


            * Deleted property `treatments` (array)
                > List of treatments applied to an observation unit.
                > 
                > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossDbId` (string)

            * Changed property `crossName` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationUnitPUI` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDbId` (string)

            * Changed property `seedLotName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

##### `POST` /observationunits

> Create new ObservationUnit


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `studyPUI` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationUnitDbId` (string)
                > The ID which uniquely identifies an observation unit
                > 
                > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


            * Deleted property `observationUnitPosition` (object)

            * Deleted property `observations` (array)
                > All observations attached to this observation unit. 
                > 
                > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


            * Deleted property `treatments` (array)
                > List of treatments applied to an observation unit.
                > 
                > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossDbId` (string)

            * Changed property `crossName` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationUnitPUI` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDbId` (string)

            * Changed property `seedLotName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

##### `GET` /observationunits/{observationUnitDbId}

> Get the details of a specific ObservationUnit


###### Parameters:

Deleted: `observationUnitDbId` in `path`
> The unique ID of the specific Observation Unit


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `germplasmPUI` (string)

        * Added property `studyPUI` (string)

        * Added property `trialPUI` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `observationUnitDbId` (string)
            > The ID which uniquely identifies an observation unit
            > 
            > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


        * Deleted property `observationUnitPosition` (object)

        * Deleted property `observations` (array)
            > All observations attached to this observation unit. 
            > 
            > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


        * Deleted property `treatments` (array)
            > List of treatments applied to an observation unit.
            > 
            > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `crossDbId` (string)

        * Changed property `crossName` (string)

        * Changed property `germplasmDbId` (string)

        * Changed property `germplasmName` (string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `observationUnitName` (string)

        * Changed property `observationUnitPUI` (string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

        * Changed property `seedLotDbId` (string)

        * Changed property `seedLotName` (string)

        * Changed property `studyDbId` (string)

        * Changed property `studyName` (string)

        * Changed property `trialDbId` (string)

        * Changed property `trialName` (string)

##### `GET` /ontologies

> Get a filtered list of Ontology


###### Parameters:

Changed: `ontologyName` in `query`
> The human readable identifier for an ontology definition.


Changed: `ontologyDbId` in `query`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
>   Use `GET /ontologies` to find the list of available ontologies on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `ontologyDbId` (string)
                > Ontology database unique identifier


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `authors` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `licence` (string)

            * Changed property `ontologyName` (string)

            * Changed property `version` (string)

##### `POST` /ontologies

> Create new Ontology


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `ontologyDbId` (string)
                > Ontology database unique identifier


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `authors` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `licence` (string)

            * Changed property `ontologyName` (string)

            * Changed property `version` (string)

##### `GET` /ontologies/{ontologyDbId}

> Get the details of a specific Ontology


###### Parameters:

Deleted: `ontologyDbId` in `path`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
> Use `GET /ontologies` to find the list of available ontologies on a server.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `ontologyDbId` (string)
            > Ontology database unique identifier


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `authors` (string)

        * Changed property `copyright` (string)

        * Changed property `description` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `licence` (string)

        * Changed property `ontologyName` (string)

        * Changed property `version` (string)

##### `PUT` /ontologies/{ontologyDbId}

> Update the details for an existing Ontology


###### Parameters:

Deleted: `ontologyDbId` in `path`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
> Use `GET /ontologies` to find the list of available ontologies on a server.


###### Request:

Changed content type : `application/json`

New required properties:
- `ontologyDbId`
- `ontologyDbId`

* Added property `ontologyDbId` (string)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `authors` (string)

* Changed property `copyright` (string)

* Changed property `description` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `licence` (string)

* Changed property `ontologyName` (string)

* Changed property `version` (string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `ontologyDbId` (string)
            > Ontology database unique identifier


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `authors` (string)

        * Changed property `copyright` (string)

        * Changed property `description` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `licence` (string)

        * Changed property `ontologyName` (string)

        * Changed property `version` (string)

##### `GET` /pedigree

> Get a filtered list of PedigreeNode


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `instituteCode` in `query`
> The code for the institute that maintains the material. 
> <br/> MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".


Added: `genu` in `query`
> List of Genus names to identify germplasm


Added: `specy` in `query`
> List of Species names to identify germplasm


Added: `includeParent` in `query`
> If this parameter is true, include the array of parents in the response


Added: `includeSibling` in `query`
> If this parameter is true, include the array of siblings in the response


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Deleted: `genus` in `query`
> The scientific genus of a germplasm


Deleted: `species` in `query`
> The scientific species of a germplasm


Deleted: `includeParents` in `query`
> If this parameter is true, include the array of parents in the response


Deleted: `includeSiblings` in `query`
> If this parameter is true, include the array of siblings in the response


Changed: `accessionNumber` in `query`
> A collection of unique identifiers for materials or germplasm within a genebank
> 
> MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").


Changed: `binomialName` in `query`
> List of the full binomial name (scientific name) to identify a germplasm


Changed: `synonym` in `query`
> List of alternative names or IDs used to reference this germplasm


Changed: `includeFullTree` in `query`
> If this parameter is true, recursively include ALL of the nodes available in this pedigree tree


Changed: `pedigreeDepth` in `query`
> Recursively include this number of levels up the tree in the response (parents, grand-parents, great-grand-parents, etc)


Changed: `progenyDepth` in `query`
> Recursively include this number of levels down the tree in the response (children, grand-children, great-grand-children, etc)


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Changed: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Changed: `germplasmPUI` in `query`
> List of Permanent Unique Identifiers to identify germplasm


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `germplasmPUI`

            * Added property `crossingProjectName` (string)

            * Added property `pedigreeNodeDbId` (string)

            * Added property `siblingDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `parents` (array)
                > A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known. 
                > <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `progeny` (array)
                > A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows 
                >       the type of parent this germplasm is to each of the child germplasm references.
                > <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `siblings` (array)
                > A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Siblings share at least one parent with the given germplasm. 
                > <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingYear` (integer -> integer)

            * Changed property `defaultDisplayName` (string)

            * Changed property `familyCode` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `pedigreeString` (string)

##### `POST` /pedigree

> Create new PedigreeNode


###### Request:

Changed content type : `application/json`

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `germplasmPUI`

            * Added property `crossingProjectName` (string)

            * Added property `pedigreeNodeDbId` (string)

            * Added property `siblingDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `parents` (array)
                > A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known. 
                > <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `progeny` (array)
                > A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows 
                >       the type of parent this germplasm is to each of the child germplasm references.
                > <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `siblings` (array)
                > A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Siblings share at least one parent with the given germplasm. 
                > <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingYear` (integer -> integer)

            * Changed property `defaultDisplayName` (string)

            * Changed property `familyCode` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `pedigreeString` (string)

##### `GET` /people

> Get a filtered list of Person


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `emailAddress` in `query`
> email address for this person


Added: `mailingAddress` in `query`
> physical address of this person


Added: `middleName` in `query`
> Persons middle name


Added: `phoneNumber` in `query`
> phone number of this person


Changed: `firstName` in `query`
> Persons first name


Changed: `lastName` in `query`
> Persons last name


Changed: `personDbId` in `query`
> Unique ID for this person


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `personDbId` (string)
                > Unique ID for a person


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `description` (string)

            * Changed property `emailAddress` (string)

            * Changed property `firstName` (string)

            * Changed property `lastName` (string)

            * Changed property `mailingAddress` (string)

            * Changed property `middleName` (string)

            * Changed property `phoneNumber` (string)

            * Changed property `userID` (string)

##### `POST` /people

> Create new Person


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `personDbId` (string)
                > Unique ID for a person


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `description` (string)

            * Changed property `emailAddress` (string)

            * Changed property `firstName` (string)

            * Changed property `lastName` (string)

            * Changed property `mailingAddress` (string)

            * Changed property `middleName` (string)

            * Changed property `phoneNumber` (string)

            * Changed property `userID` (string)

##### `GET` /people/{personDbId}

> Get the details of a specific Person


###### Parameters:

Deleted: `personDbId` in `path`
> The unique ID of a person


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `personDbId` (string)
            > Unique ID for a person


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `description` (string)

        * Changed property `emailAddress` (string)

        * Changed property `firstName` (string)

        * Changed property `lastName` (string)

        * Changed property `mailingAddress` (string)

        * Changed property `middleName` (string)

        * Changed property `phoneNumber` (string)

        * Changed property `userID` (string)

##### `PUT` /people/{personDbId}

> Update the details for an existing Person


###### Parameters:

Deleted: `personDbId` in `path`
> The unique ID of a person


###### Request:

Changed content type : `application/json`

New required properties:
- `personDbId`
- `personDbId`

* Added property `personDbId` (string)

* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `description` (string)

* Changed property `emailAddress` (string)

* Changed property `firstName` (string)

* Changed property `lastName` (string)

* Changed property `mailingAddress` (string)

* Changed property `middleName` (string)

* Changed property `phoneNumber` (string)

* Changed property `userID` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `personDbId` (string)
            > Unique ID for a person


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `description` (string)

        * Changed property `emailAddress` (string)

        * Changed property `firstName` (string)

        * Changed property `lastName` (string)

        * Changed property `mailingAddress` (string)

        * Changed property `middleName` (string)

        * Changed property `phoneNumber` (string)

        * Changed property `userID` (string)

##### `GET` /plates

> Get a filtered list of Plate


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `plateBarcode` in `query`
> A unique identifier physically attached to the plate


Added: `germplasmDbId` in `query`
> The ID which uniquely identifies a germplasm


Changed: `sampleDbId` in `query`
> The ID which uniquely identifies a sample


Changed: `sampleName` in `query`
> The human readable name of the sample


Changed: `sampleGroupDbId` in `query`
> The unique identifier for a group of related Samples


Changed: `observationUnitDbId` in `query`
> The ID which uniquely identifies an observation unit


Changed: `plateDbId` in `query`
> The ID which uniquely identifies a plate of samples


Changed: `plateName` in `query`
> The human readable name of a plate of samples


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `programName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `plateDbId` (string)
                > The ID which uniquely identifies a `Plate`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `plateBarcode` (string)

            * Changed property `plateFormat` (string)
                > Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format


            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `sampleType` (string)
                > The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc


            * Changed property `studyDbId` (string)

            * Changed property `trialDbId` (string)

##### `POST` /plates

> Create new Plate


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `programName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `plateDbId` (string)
                > The ID which uniquely identifies a `Plate`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `plateBarcode` (string)

            * Changed property `plateFormat` (string)
                > Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format


            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `sampleType` (string)
                > The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc


            * Changed property `studyDbId` (string)

            * Changed property `trialDbId` (string)

##### `GET` /plates/{plateDbId}

> Get the details of a specific Plate


###### Parameters:

Deleted: `plateDbId` in `path`
> The ID which uniquely identifies a `Plate`


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `programName` (string)

        * Added property `studyName` (string)

        * Added property `studyPUI` (string)

        * Added property `trialName` (string)

        * Added property `trialPUI` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `plateDbId` (string)
            > The ID which uniquely identifies a `Plate`


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `plateBarcode` (string)

        * Changed property `plateFormat` (string)
            > Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format


        * Changed property `plateName` (string)

        * Changed property `programDbId` (string)

        * Changed property `sampleType` (string)
            > The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc


        * Changed property `studyDbId` (string)

        * Changed property `trialDbId` (string)

##### `GET` /programs

> Get a filtered list of Program


###### Parameters:

Added: `leadPersonDbId` in `query`
> The person DbIds of the program leader to search for


Added: `leadPersonName` in `query`
> The names of the program leader to search for


Added: `objectife` in `query`
> A program objective to search for


Changed: `abbreviation` in `query`
> A list of shortened human readable names for a set of Programs


Changed: `programType` in `query`
> The type of program entity this object represents
> <br/> 'STANDARD' represents a standard, permanent breeding program
> <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `leadPersonDbId` (string)
                > The unique identifier of the program leader


            * Deleted property `leadPersonName` (string)
                > The name of the program leader


            * Deleted property `programDbId` (string)
                > The ID which uniquely identifies the program


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `fundingInformation` (string)

            * Changed property `objective` (string)

            * Changed property `programName` (string)

            * Changed property `programType` (string)
                > The type of program entity this object represents
                > <br/> 'STANDARD' represents a standard, permanent breeding program
                > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


##### `POST` /programs

> Create new Program


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `leadPersonDbId` (string)
                > The unique identifier of the program leader


            * Deleted property `leadPersonName` (string)
                > The name of the program leader


            * Deleted property `programDbId` (string)
                > The ID which uniquely identifies the program


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `fundingInformation` (string)

            * Changed property `objective` (string)

            * Changed property `programName` (string)

            * Changed property `programType` (string)
                > The type of program entity this object represents
                > <br/> 'STANDARD' represents a standard, permanent breeding program
                > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


##### `GET` /programs/{programDbId}

> Get the details of a specific Program


###### Parameters:

Deleted: `programDbId` in `path`
> Filter by the common crop name. Exact match.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `personDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `leadPersonDbId` (string)
            > The unique identifier of the program leader


        * Deleted property `leadPersonName` (string)
            > The name of the program leader


        * Deleted property `programDbId` (string)
            > The ID which uniquely identifies the program


        * Changed property `abbreviation` (string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `fundingInformation` (string)

        * Changed property `objective` (string)

        * Changed property `programName` (string)

        * Changed property `programType` (string)
            > The type of program entity this object represents
            > <br/> 'STANDARD' represents a standard, permanent breeding program
            > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


##### `PUT` /programs/{programDbId}

> Update the details for an existing Program


###### Parameters:

Deleted: `programDbId` in `path`
> Filter by the common crop name. Exact match.


###### Request:

Changed content type : `application/json`

New required properties:
- `programDbId`
- `programDbId`

* Added property `personDbId` (string)

* Added property `programDbId` (string)

* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `leadPersonDbId` (string)
    > The unique identifier of the program leader


* Deleted property `leadPersonName` (string)
    > The name of the program leader


* Changed property `abbreviation` (string)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `commonCropName` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `fundingInformation` (string)

* Changed property `objective` (string)

* Changed property `programName` (string)

* Changed property `programType` (string)
    > The type of program entity this object represents
    > <br/> 'STANDARD' represents a standard, permanent breeding program
    > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `personDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `leadPersonDbId` (string)
            > The unique identifier of the program leader


        * Deleted property `leadPersonName` (string)
            > The name of the program leader


        * Deleted property `programDbId` (string)
            > The ID which uniquely identifies the program


        * Changed property `abbreviation` (string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `fundingInformation` (string)

        * Changed property `objective` (string)

        * Changed property `programName` (string)

        * Changed property `programType` (string)
            > The type of program entity this object represents
            > <br/> 'STANDARD' represents a standard, permanent breeding program
            > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


##### `GET` /samples

> Get a filtered list of Sample


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `germplasmDbId` in `query`
> The ID which uniquely identifies a `Germplasm`


Changed: `sampleDbId` in `query`
> The ID which uniquely identifies a `Sample`


Changed: `plateDbId` in `query`
> The ID which uniquely identifies a `Plate` of `Samples`


Changed: `plateName` in `query`
> The human readable name of a `Plate` of `Samples`


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `sampleDbId`

            * Added property `callSetDbIds` (array)

            * Added property `germplasmName` (string)

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `programName` (string)

            * Added property `sampleGroupId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `sampleGroupDbId` (string)
                > The ID which uniquely identifies a group of `Samples`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `column` (integer -> integer)

            * Changed property `germplasmDbId` (string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `plateDbId` (string)

            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `row` (string)

            * Changed property `sampleBarcode` (string)

            * Changed property `sampleDescription` (string)

            * Changed property `sampleName` (string)

            * Changed property `samplePUI` (string)

            * Changed property `sampleTimestamp` (string -> string)

            * Changed property `sampleType` (string)

            * Changed property `studyDbId` (string)

            * Changed property `takenBy` (string)

            * Changed property `tissueType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `well` (string)

##### `PUT` /samples

> Update the details for an existing Sample


###### Request:

Changed content type : `application/json`

New required properties:
- `sampleDbId`
- `sampleName`

* Added property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


* Added property `callSetDbIds` (array)

* Added property `column` (integer)

* Added property `germplasmDbId` (string)

* Added property `germplasmName` (string)

* Added property `germplasmPUI` (string)

* Added property `observationUnitDbId` (string)

* Added property `observationUnitName` (string)

* Added property `observationUnitPUI` (string)

* Added property `plateDbId` (string)

* Added property `plateName` (string)

* Added property `programDbId` (string)

* Added property `programName` (string)

* Added property `row` (string)

* Added property `sampleBarcode` (string)

* Added property `sampleDbId` (string)

* Added property `sampleDescription` (string)

* Added property `sampleGroupId` (string)

* Added property `sampleName` (string)

* Added property `samplePUI` (string)

* Added property `sampleTimestamp` (string)

* Added property `sampleType` (string)

* Added property `studyDbId` (string)

* Added property `studyName` (string)

* Added property `studyPUI` (string)

* Added property `takenBy` (string)

* Added property `tissueType` (string)

* Added property `trialDbId` (string)

* Added property `trialName` (string)

* Added property `trialPUI` (string)

* Added property `well` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `sampleDbId`

            * Added property `callSetDbIds` (array)

            * Added property `germplasmName` (string)

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `programName` (string)

            * Added property `sampleGroupId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `sampleGroupDbId` (string)
                > The ID which uniquely identifies a group of `Samples`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `column` (integer -> integer)

            * Changed property `germplasmDbId` (string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `plateDbId` (string)

            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `row` (string)

            * Changed property `sampleBarcode` (string)

            * Changed property `sampleDescription` (string)

            * Changed property `sampleName` (string)

            * Changed property `samplePUI` (string)

            * Changed property `sampleTimestamp` (string -> string)

            * Changed property `sampleType` (string)

            * Changed property `studyDbId` (string)

            * Changed property `takenBy` (string)

            * Changed property `tissueType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `well` (string)

##### `POST` /samples

> Create new Sample


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `sampleDbId`

            * Added property `callSetDbIds` (array)

            * Added property `germplasmName` (string)

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `programName` (string)

            * Added property `sampleGroupId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `sampleGroupDbId` (string)
                > The ID which uniquely identifies a group of `Samples`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `column` (integer -> integer)

            * Changed property `germplasmDbId` (string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `plateDbId` (string)

            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `row` (string)

            * Changed property `sampleBarcode` (string)

            * Changed property `sampleDescription` (string)

            * Changed property `sampleName` (string)

            * Changed property `samplePUI` (string)

            * Changed property `sampleTimestamp` (string -> string)

            * Changed property `sampleType` (string)

            * Changed property `studyDbId` (string)

            * Changed property `takenBy` (string)

            * Changed property `tissueType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `well` (string)

##### `GET` /samples/{sampleDbId}


###### Parameters:

Deleted: `sampleDbId` in `path`
> The unique identifier for a `Sample`


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `sampleDbId`

        * Added property `callSetDbIds` (array)

        * Added property `germplasmName` (string)

        * Added property `germplasmPUI` (string)

        * Added property `observationUnitName` (string)

        * Added property `observationUnitPUI` (string)

        * Added property `programName` (string)

        * Added property `sampleGroupId` (string)

        * Added property `studyName` (string)

        * Added property `studyPUI` (string)

        * Added property `trialName` (string)

        * Added property `trialPUI` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `sampleGroupDbId` (string)
            > The ID which uniquely identifies a group of `Samples`


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `column` (integer -> integer)

        * Changed property `germplasmDbId` (string)

        * Changed property `observationUnitDbId` (string)

        * Changed property `plateDbId` (string)

        * Changed property `plateName` (string)

        * Changed property `programDbId` (string)

        * Changed property `row` (string)

        * Changed property `sampleBarcode` (string)

        * Changed property `sampleDescription` (string)

        * Changed property `sampleName` (string)

        * Changed property `samplePUI` (string)

        * Changed property `sampleTimestamp` (string -> string)

        * Changed property `sampleType` (string)

        * Changed property `studyDbId` (string)

        * Changed property `takenBy` (string)

        * Changed property `tissueType` (string)

        * Changed property `trialDbId` (string)

        * Changed property `well` (string)

##### `POST` /search/allelematrix

> Submit a search request for `AlleleMatrix`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `result` (object)

        New required properties:
        - `data`

        New optional properties:
        - `callSetDbIds`
        - `variantSetDbIds`

        * Added property `data` (array)

            Items (object):

            * Property `callSetDbIds` (array)

            * Property `expandHomozygotes` (boolean)

            * Property `sepPhased` (string)

            * Property `sepUnphased` (string)

            * Property `unknownString` (string)

            * Property `variantDbIds` (array)

            * Property `variantSetDbIds` (array)

        * Deleted property `callSetDbIds` (array)
            > A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.


        * Deleted property `dataMatrices` (array)
            > The 'dataMatrices' are an array of matrix objects that hold the allele data and associated metadata. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.


        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `pagination` (array)
            > Pagination for the matrix


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Deleted property `variantDbIds` (array)
            > A list of unique identifiers for the Variants contained in the matrix response. This array should match the ordering for rows in the matrix.


        * Deleted property `variantSetDbIds` (array)
            > A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.


    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/allelematrix/{searchResultsDbId}

> Submit a search request for `AlleleMatrix`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/alleleMatrix/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `result` (object)

        New required properties:
        - `data`

        New optional properties:
        - `callSetDbIds`
        - `variantSetDbIds`

        * Added property `data` (array)

        * Deleted property `callSetDbIds` (array)
            > A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.


        * Deleted property `dataMatrices` (array)
            > The 'dataMatrices' are an array of matrix objects that hold the allele data and associated metadata. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.


        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `pagination` (array)
            > Pagination for the matrix


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Deleted property `variantDbIds` (array)
            > A list of unique identifiers for the Variants contained in the matrix response. This array should match the ordering for rows in the matrix.


        * Deleted property `variantSetDbIds` (array)
            > A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.


    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `POST` /search/attributes

> Submit a search request for `GermplasmAttribute`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `attributeValueDbIds` (array)

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `attributeDbId` (string)
                > The ID which uniquely identifies this attribute within the given database server


            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeCategory` (string)

            * Changed property `attributeDescription` (string)

            * Changed property `attributeName` (string)

            * Changed property `attributePUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/attributes/{searchResultsDbId}

> Submit a search request for `GermplasmAttribute`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/germplasmAttribute/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `attributeValueDbIds` (array)

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `attributeDbId` (string)
                > The ID which uniquely identifies this attribute within the given database server


            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeCategory` (string)

            * Changed property `attributeDescription` (string)

            * Changed property `attributeName` (string)

            * Changed property `attributePUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `POST` /search/attributevalues

> Submit a search request for `GermplasmAttributeValue`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `attributePUI` (string)

            * Added property `germplasmPUI` (string)

            * Deleted property `attributeValueDbId` (string)
                > The ID which uniquely identifies this attribute value within the given database server


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeDbId` (string)

            * Changed property `attributeName` (string)

            * Changed property `determinedDate` (string -> string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `value` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/attributevalues/{searchResultsDbId}

> Submit a search request for `GermplasmAttributeValue`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/germplasmAttributeValue/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `attributePUI` (string)

            * Added property `germplasmPUI` (string)

            * Deleted property `attributeValueDbId` (string)
                > The ID which uniquely identifies this attribute value within the given database server


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attributeDbId` (string)

            * Changed property `attributeName` (string)

            * Changed property `determinedDate` (string -> string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `value` (string)

##### `POST` /search/calls

> Submit a search request for `Call`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/calls/{searchResultsDbId}

> Submit a search request for `Call`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/call/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `POST` /search/callsets

> Submit a search request for `CallSet`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleName` (string)

            * Added property `samplePUI` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `created` (string -> string)

            * Changed property `sampleDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `updated` (string -> string)

            * Changed property `variantSetDbIds` (array)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/callsets/{searchResultsDbId}

> Submit a search request for `CallSet`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/callSet/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleName` (string)

            * Added property `samplePUI` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `created` (string -> string)

            * Changed property `sampleDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `updated` (string -> string)

            * Changed property `variantSetDbIds` (array)

##### `POST` /search/germplasm


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleDbIds` (array)

            * Deleted property `donors` (array)
                > List of donor institutes


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `germplasmDbId` (string)
                > The ID which uniquely identifies a germplasm within the given database server 
                > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


            * Deleted property `germplasmOrigin` (array)
                > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


            * Deleted property `storageTypes` (array)
                > The type of storage this germplasm is kept in at a genebank.


            * Deleted property `synonyms` (array)
                > List of alternative names or IDs used to reference this germplasm
                > 
                > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


            * Deleted property `taxonIds` (array)
                > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
                > 
                > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


            * Changed property `accessionNumber` (string)

            * Changed property `acquisitionDate` (string -> string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `biologicalStatusOfAccessionCode` (string)
                > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
                > 
                > 100) Wild 
                > 110) Natural 
                > 120) Semi-natural/wild 
                > 130) Semi-natural/sown 
                > 200) Weedy 
                > 300) Traditional cultivar/landrace 
                > 400) Breeding/research material 
                > 410) Breeders line 
                > 411) Synthetic population 
                > 412) Hybrid 
                > 413) Founder stock/base population 
                > 414) Inbred line (parent of hybrid cultivar) 
                > 415) Segregating population 
                > 416) Clonal selection 
                > 420) Genetic stock 
                > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
                > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
                > 423) Other genetic stocks (e.g. mapping populations) 
                > 500) Advanced or improved cultivar (conventional breeding methods) 
                > 600) GMO (by genetic engineering) 
                > 999) Other (Elaborate in REMARKS field)


            * Changed property `biologicalStatusOfAccessionDescription` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `collection` (string)

            * Changed property `commonCropName` (string)

            * Changed property `countryOfOriginCode` (string)

            * Changed property `defaultDisplayName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `genus` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `germplasmPreprocessing` (string)

            * Changed property `instituteCode` (string)

            * Changed property `instituteName` (string)

            * Changed property `pedigree` (string)

            * Changed property `seedSource` (string)

            * Changed property `seedSourceDescription` (string)

            * Changed property `species` (string)

            * Changed property `speciesAuthority` (string)

            * Changed property `subtaxa` (string)

            * Changed property `subtaxaAuthority` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/germplasm/{searchResultsDbId}

> Submit a search request for `Germplasm`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/germplasm/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleDbIds` (array)

            * Deleted property `donors` (array)
                > List of donor institutes


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `germplasmDbId` (string)
                > The ID which uniquely identifies a germplasm within the given database server 
                > <br>MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.


            * Deleted property `germplasmOrigin` (array)
                > Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.


            * Deleted property `storageTypes` (array)
                > The type of storage this germplasm is kept in at a genebank.


            * Deleted property `synonyms` (array)
                > List of alternative names or IDs used to reference this germplasm
                > 
                > MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.


            * Deleted property `taxonIds` (array)
                > The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.
                > 
                > MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.


            * Changed property `accessionNumber` (string)

            * Changed property `acquisitionDate` (string -> string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `biologicalStatusOfAccessionCode` (string)
                > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
                > 
                > 100) Wild 
                > 110) Natural 
                > 120) Semi-natural/wild 
                > 130) Semi-natural/sown 
                > 200) Weedy 
                > 300) Traditional cultivar/landrace 
                > 400) Breeding/research material 
                > 410) Breeders line 
                > 411) Synthetic population 
                > 412) Hybrid 
                > 413) Founder stock/base population 
                > 414) Inbred line (parent of hybrid cultivar) 
                > 415) Segregating population 
                > 416) Clonal selection 
                > 420) Genetic stock 
                > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
                > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
                > 423) Other genetic stocks (e.g. mapping populations) 
                > 500) Advanced or improved cultivar (conventional breeding methods) 
                > 600) GMO (by genetic engineering) 
                > 999) Other (Elaborate in REMARKS field)


            * Changed property `biologicalStatusOfAccessionDescription` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `collection` (string)

            * Changed property `commonCropName` (string)

            * Changed property `countryOfOriginCode` (string)

            * Changed property `defaultDisplayName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `genus` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `germplasmPreprocessing` (string)

            * Changed property `instituteCode` (string)

            * Changed property `instituteName` (string)

            * Changed property `pedigree` (string)

            * Changed property `seedSource` (string)

            * Changed property `seedSourceDescription` (string)

            * Changed property `species` (string)

            * Changed property `speciesAuthority` (string)

            * Changed property `subtaxa` (string)

            * Changed property `subtaxaAuthority` (string)

##### `POST` /search/lists

> Submit a search request for `List`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `listDbId` (string)
                > The unique identifier for a List


            * Deleted property `listOwnerPersonDbId` (string)
                > The unique identifier for a List Owner. (usually a user or person)


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dateCreated` (string -> string)

            * Changed property `dateModified` (string -> string)

            * Changed property `listDescription` (string)

            * Changed property `listName` (string)

            * Changed property `listOwnerName` (string)

            * Changed property `listSize` (integer -> integer)

            * Changed property `listSource` (string)

            * Changed property `listType` (string)
                > The type of objects that are referenced in a List


Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/lists/{searchResultsDbId}

> Submit a search request for `List`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/list/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `listDbId` (string)
                > The unique identifier for a List


            * Deleted property `listOwnerPersonDbId` (string)
                > The unique identifier for a List Owner. (usually a user or person)


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dateCreated` (string -> string)

            * Changed property `dateModified` (string -> string)

            * Changed property `listDescription` (string)

            * Changed property `listName` (string)

            * Changed property `listOwnerName` (string)

            * Changed property `listSize` (integer -> integer)

            * Changed property `listSource` (string)

            * Changed property `listType` (string)
                > The type of objects that are referenced in a List


##### `POST` /search/markerpositions

> Submit a search request for `MarkerPosition`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `mapPUI` (string)

            * Deleted property `variantName` (string)
                > The human readable name for a `Variant`
                > <br> A `Variant` can also represent a Marker


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `linkageGroupName` (string)

            * Changed property `mapDbId` (string)

            * Changed property `mapName` (string)

            * Changed property `position` (integer -> integer)

            * Changed property `variantDbId` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/markerpositions/{searchResultsDbId}

> Submit a search request for `MarkerPosition`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/markerPosition/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `mapPUI` (string)

            * Deleted property `variantName` (string)
                > The human readable name for a `Variant`
                > <br> A `Variant` can also represent a Marker


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `linkageGroupName` (string)

            * Changed property `mapDbId` (string)

            * Changed property `mapName` (string)

            * Changed property `position` (integer -> integer)

            * Changed property `variantDbId` (string)

##### `POST` /search/observationunits

> Submit a search request for `ObservationUnit`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `studyPUI` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationUnitDbId` (string)
                > The ID which uniquely identifies an observation unit
                > 
                > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


            * Deleted property `observationUnitPosition` (object)

            * Deleted property `observations` (array)
                > All observations attached to this observation unit. 
                > 
                > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


            * Deleted property `treatments` (array)
                > List of treatments applied to an observation unit.
                > 
                > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossDbId` (string)

            * Changed property `crossName` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationUnitPUI` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDbId` (string)

            * Changed property `seedLotName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/observationunits/{searchResultsDbId}

> Submit a search request for `ObservationUnit`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/observationUnit/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `studyPUI` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationUnitDbId` (string)
                > The ID which uniquely identifies an observation unit
                > 
                > MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.


            * Deleted property `observationUnitPosition` (object)

            * Deleted property `observations` (array)
                > All observations attached to this observation unit. 
                > 
                > Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.


            * Deleted property `treatments` (array)
                > List of treatments applied to an observation unit.
                > 
                > MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossDbId` (string)

            * Changed property `crossName` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationUnitPUI` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDbId` (string)

            * Changed property `seedLotName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `studyName` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

##### `POST` /search/pedigree

> Submit a search request for `PedigreeNode`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `germplasmPUI`

            * Added property `crossingProjectName` (string)

            * Added property `pedigreeNodeDbId` (string)

            * Added property `siblingDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `parents` (array)
                > A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known. 
                > <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `progeny` (array)
                > A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows 
                >       the type of parent this germplasm is to each of the child germplasm references.
                > <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `siblings` (array)
                > A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Siblings share at least one parent with the given germplasm. 
                > <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingYear` (integer -> integer)

            * Changed property `defaultDisplayName` (string)

            * Changed property `familyCode` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `pedigreeString` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/pedigree/{searchResultsDbId}

> Submit a search request for `PedigreeNode`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/pedigreeNode/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `germplasmPUI`

            * Added property `crossingProjectName` (string)

            * Added property `pedigreeNodeDbId` (string)

            * Added property `siblingDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `parents` (array)
                > A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known. 
                > <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `progeny` (array)
                > A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows 
                >       the type of parent this germplasm is to each of the child germplasm references.
                > <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.


            * Deleted property `siblings` (array)
                > A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes.
                > <br/> Siblings share at least one parent with the given germplasm. 
                > <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `breedingMethodDbId` (string)

            * Changed property `breedingMethodName` (string)

            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingYear` (integer -> integer)

            * Changed property `defaultDisplayName` (string)

            * Changed property `familyCode` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `germplasmPUI` (string)

            * Changed property `pedigreeString` (string)

##### `POST` /search/people

> Submit a search request for `Person`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `personDbId` (string)
                > Unique ID for a person


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `description` (string)

            * Changed property `emailAddress` (string)

            * Changed property `firstName` (string)

            * Changed property `lastName` (string)

            * Changed property `mailingAddress` (string)

            * Changed property `middleName` (string)

            * Changed property `phoneNumber` (string)

            * Changed property `userID` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/people/{searchResultsDbId}

> Submit a search request for `Person`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/person/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `personDbId` (string)
                > Unique ID for a person


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `description` (string)

            * Changed property `emailAddress` (string)

            * Changed property `firstName` (string)

            * Changed property `lastName` (string)

            * Changed property `mailingAddress` (string)

            * Changed property `middleName` (string)

            * Changed property `phoneNumber` (string)

            * Changed property `userID` (string)

##### `POST` /search/plates

> Submit a search request for `Plate`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `programName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `plateDbId` (string)
                > The ID which uniquely identifies a `Plate`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `plateBarcode` (string)

            * Changed property `plateFormat` (string)
                > Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format


            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `sampleType` (string)
                > The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc


            * Changed property `studyDbId` (string)

            * Changed property `trialDbId` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/plates/{searchResultsDbId}

> Submit a search request for `Plate`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/plate/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `programName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `plateDbId` (string)
                > The ID which uniquely identifies a `Plate`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `plateBarcode` (string)

            * Changed property `plateFormat` (string)
                > Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format


            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `sampleType` (string)
                > The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc


            * Changed property `studyDbId` (string)

            * Changed property `trialDbId` (string)

##### `POST` /search/programs

> Submit a search request for `Program`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `leadPersonDbId` (string)
                > The unique identifier of the program leader


            * Deleted property `leadPersonName` (string)
                > The name of the program leader


            * Deleted property `programDbId` (string)
                > The ID which uniquely identifies the program


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `fundingInformation` (string)

            * Changed property `objective` (string)

            * Changed property `programName` (string)

            * Changed property `programType` (string)
                > The type of program entity this object represents
                > <br/> 'STANDARD' represents a standard, permanent breeding program
                > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/programs/{searchResultsDbId}

> Submit a search request for `Program`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/program/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `personDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `leadPersonDbId` (string)
                > The unique identifier of the program leader


            * Deleted property `leadPersonName` (string)
                > The name of the program leader


            * Deleted property `programDbId` (string)
                > The ID which uniquely identifies the program


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `fundingInformation` (string)

            * Changed property `objective` (string)

            * Changed property `programName` (string)

            * Changed property `programType` (string)
                > The type of program entity this object represents
                > <br/> 'STANDARD' represents a standard, permanent breeding program
                > <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding


##### `POST` /search/samples

> Submit a search request for `Sample`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `sampleDbId`

            * Added property `callSetDbIds` (array)

            * Added property `germplasmName` (string)

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `programName` (string)

            * Added property `sampleGroupId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `sampleGroupDbId` (string)
                > The ID which uniquely identifies a group of `Samples`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `column` (integer -> integer)

            * Changed property `germplasmDbId` (string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `plateDbId` (string)

            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `row` (string)

            * Changed property `sampleBarcode` (string)

            * Changed property `sampleDescription` (string)

            * Changed property `sampleName` (string)

            * Changed property `samplePUI` (string)

            * Changed property `sampleTimestamp` (string -> string)

            * Changed property `sampleType` (string)

            * Changed property `studyDbId` (string)

            * Changed property `takenBy` (string)

            * Changed property `tissueType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `well` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/samples/{searchResultsDbId}

> Submit a search request for `Sample`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/sample/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `sampleDbId`

            * Added property `callSetDbIds` (array)

            * Added property `germplasmName` (string)

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `programName` (string)

            * Added property `sampleGroupId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Added property `trialName` (string)

            * Added property `trialPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `sampleGroupDbId` (string)
                > The ID which uniquely identifies a group of `Samples`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `column` (integer -> integer)

            * Changed property `germplasmDbId` (string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `plateDbId` (string)

            * Changed property `plateName` (string)

            * Changed property `programDbId` (string)

            * Changed property `row` (string)

            * Changed property `sampleBarcode` (string)

            * Changed property `sampleDescription` (string)

            * Changed property `sampleName` (string)

            * Changed property `samplePUI` (string)

            * Changed property `sampleTimestamp` (string -> string)

            * Changed property `sampleType` (string)

            * Changed property `studyDbId` (string)

            * Changed property `takenBy` (string)

            * Changed property `tissueType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `well` (string)

##### `POST` /search/variables

> Submit a search request for `ObservationVariable`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `observationVariableDbId` (string)
                > Variable unique identifier
                > 
                > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `observationVariablePUI` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/variables/{searchResultsDbId}

> Submit a search request for `ObservationVariable`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/observationVariable/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `observationVariableDbId` (string)
                > Variable unique identifier
                > 
                > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `observationVariablePUI` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `POST` /search/variants

> Submit a search request for `Variant`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `variantSetName` (string)

            * Deleted property `alternateBases` (array)
                > The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `alternate_bases` (array)
                > **Deprecated in v2.1** Please use `alternateBases`. Github issue number #549
                > <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `ciend` (array)
                > Similar to "cipos", but for the variant's end position (which is derived from start + svlen).


            * Deleted property `cipos` (array)
                > In the case of structural variants, start and end of the variant may not
                > be known with an exact base position. "cipos" provides an interval with
                > high confidence for the start position. The interval is provided by 0 or
                > 2 signed integers which are added to the start position.
                > Based on the use in VCF v4.2


            * Deleted property `externalReferences` (object)

            * Deleted property `filtersFailed` (array)
                > Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.


            * Deleted property `variantNames` (array)
                > A human readable name associated with a `Variant`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `created` (string -> string)

            * Changed property `end` (integer -> integer)

            * Changed property `filtersApplied` (boolean -> boolean)

            * Changed property `filtersPassed` (boolean -> boolean)

            * Changed property `referenceBases` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `start` (integer -> integer)

            * Changed property `svlen` (integer -> integer)

            * Changed property `updated` (string -> string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (array -> string)

            * Changed property `variantType` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/variants/{searchResultsDbId}

> Submit a search request for `Variant`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/variant/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `variantSetName` (string)

            * Deleted property `alternateBases` (array)
                > The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `alternate_bases` (array)
                > **Deprecated in v2.1** Please use `alternateBases`. Github issue number #549
                > <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `ciend` (array)
                > Similar to "cipos", but for the variant's end position (which is derived from start + svlen).


            * Deleted property `cipos` (array)
                > In the case of structural variants, start and end of the variant may not
                > be known with an exact base position. "cipos" provides an interval with
                > high confidence for the start position. The interval is provided by 0 or
                > 2 signed integers which are added to the start position.
                > Based on the use in VCF v4.2


            * Deleted property `externalReferences` (object)

            * Deleted property `filtersFailed` (array)
                > Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.


            * Deleted property `variantNames` (array)
                > A human readable name associated with a `Variant`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `created` (string -> string)

            * Changed property `end` (integer -> integer)

            * Changed property `filtersApplied` (boolean -> boolean)

            * Changed property `filtersPassed` (boolean -> boolean)

            * Changed property `referenceBases` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `start` (integer -> integer)

            * Changed property `svlen` (integer -> integer)

            * Changed property `updated` (string -> string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (array -> string)

            * Changed property `variantType` (string)

##### `POST` /search/variantsets

> Submit a search request for `VariantSet`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `analysiDbIds` (array)

            * Added property `referenceSetName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `analysis` (array)
                > Set of Analysis descriptors for this VariantSet


            * Deleted property `availableFormats` (array)
                > When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats. 
                > <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)
                > <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.


            * Deleted property `externalReferences` (object)

            * Deleted property `metadataFields` (array)
                > The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet. 
                > <br> When possible, these field names and abbreviations should follow the VCF standard


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetCount` (integer -> integer)

            * Changed property `referenceSetDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `variantCount` (integer -> integer)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


##### `GET` /search/variantsets/{searchResultsDbId}

> Submit a search request for `VariantSet`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/variantSet/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `analysiDbIds` (array)

            * Added property `referenceSetName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `analysis` (array)
                > Set of Analysis descriptors for this VariantSet


            * Deleted property `availableFormats` (array)
                > When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats. 
                > <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)
                > <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.


            * Deleted property `externalReferences` (object)

            * Deleted property `metadataFields` (array)
                > The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet. 
                > <br> When possible, these field names and abbreviations should follow the VCF standard


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetCount` (integer -> integer)

            * Changed property `referenceSetDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `variantCount` (integer -> integer)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /seasons

> Get a filtered list of Season


###### Parameters:

Changed: `seasonDbId` in `query`
> The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'.


Changed: `season` in `query`
> The term to describe a given season. Example "Spring" OR "May" OR "Planting_Time_7".


Changed: `seasonName` in `query`
> The term to describe a given season. Example "Spring" OR "May" OR "Planting_Time_7".


Changed: `year` in `query`
> The 4 digit year of a season. Example "2017"


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Changed property `seasonDbId` (string)

            * Changed property `seasonName` (string)

            * Changed property `year` (integer -> integer)

##### `POST` /seasons

> Create new Season


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Changed property `seasonDbId` (string)

            * Changed property `seasonName` (string)

            * Changed property `year` (integer -> integer)

##### `GET` /seasons/{seasonDbId}

> Get the details of a specific Season


###### Parameters:

Deleted: `seasonDbId` in `path`
> The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `seasonDbId` (string)

        * Changed property `seasonName` (string)

        * Changed property `year` (integer -> integer)

##### `PUT` /seasons/{seasonDbId}

> Update the details for an existing Season


###### Parameters:

Deleted: `seasonDbId` in `path`
> The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'


###### Request:

Changed content type : `application/json`

* Changed property `seasonDbId` (string)

* Changed property `seasonName` (string)

* Changed property `year` (integer -> integer)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `seasonDbId` (string)

        * Changed property `seasonName` (string)

        * Changed property `year` (integer -> integer)

##### `GET` /seedlots

> Get a filtered list of SeedLot


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Changed: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `contentMixture` (array)
                > The mixture of germplasm present in the seed lot.
                > <br/>
                > If this seed lot only contains a single germplasm, the response should contain the name 
                > and DbId of that germplasm with a mixturePercentage value of 100
                > <br/>
                > If the seed lot contains a mixture of different germplasm, the response should contain 
                > the name and DbId every germplasm present. The mixturePercentage field should contain 
                > the ratio of each germplasm in the total mixture. All of the mixturePercentage values 
                > in this array should sum to equal 100.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `seedLotDbId` (string)
                > Unique DbId for the Seed Lot


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `amount` (number)

            * Changed property `createdDate` (string -> string)

            * Changed property `lastUpdated` (string -> string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDescription` (string)

            * Changed property `seedLotName` (string)

            * Changed property `sourceCollection` (string)

            * Changed property `storageLocation` (string)

            * Changed property `units` (string)

##### `POST` /seedlots

> Create new SeedLot


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `contentMixture` (array)
                > The mixture of germplasm present in the seed lot.
                > <br/>
                > If this seed lot only contains a single germplasm, the response should contain the name 
                > and DbId of that germplasm with a mixturePercentage value of 100
                > <br/>
                > If the seed lot contains a mixture of different germplasm, the response should contain 
                > the name and DbId every germplasm present. The mixturePercentage field should contain 
                > the ratio of each germplasm in the total mixture. All of the mixturePercentage values 
                > in this array should sum to equal 100.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `seedLotDbId` (string)
                > Unique DbId for the Seed Lot


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `amount` (number)

            * Changed property `createdDate` (string -> string)

            * Changed property `lastUpdated` (string -> string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `seedLotDescription` (string)

            * Changed property `seedLotName` (string)

            * Changed property `sourceCollection` (string)

            * Changed property `storageLocation` (string)

            * Changed property `units` (string)

##### `GET` /seedlots/{seedLotDbId}

> Get the details of a specific SeedLot


###### Parameters:

Deleted: `seedLotDbId` in `path`
> Unique id for a seed lot on this server


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `contentMixture` (array)
            > The mixture of germplasm present in the seed lot.
            > <br/>
            > If this seed lot only contains a single germplasm, the response should contain the name 
            > and DbId of that germplasm with a mixturePercentage value of 100
            > <br/>
            > If the seed lot contains a mixture of different germplasm, the response should contain 
            > the name and DbId every germplasm present. The mixturePercentage field should contain 
            > the ratio of each germplasm in the total mixture. All of the mixturePercentage values 
            > in this array should sum to equal 100.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `seedLotDbId` (string)
            > Unique DbId for the Seed Lot


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `amount` (number)

        * Changed property `createdDate` (string -> string)

        * Changed property `lastUpdated` (string -> string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

        * Changed property `seedLotDescription` (string)

        * Changed property `seedLotName` (string)

        * Changed property `sourceCollection` (string)

        * Changed property `storageLocation` (string)

        * Changed property `units` (string)

##### `PUT` /seedlots/{seedLotDbId}

> Update the details for an existing SeedLot


###### Parameters:

Deleted: `seedLotDbId` in `path`
> Unique id for a seed lot on this server


###### Request:

Changed content type : `application/json`

New required properties:
- `seedLotDbId`
- `seedLotDbId`

* Added property `seedLotDbId` (string)

* Deleted property `contentMixture` (array)
    > The mixture of germplasm present in the seed lot.
    > <br/>
    > If this seed lot only contains a single germplasm, the response should contain the name 
    > and DbId of that germplasm with a mixturePercentage value of 100
    > <br/>
    > If the seed lot contains a mixture of different germplasm, the response should contain 
    > the name and DbId every germplasm present. The mixturePercentage field should contain 
    > the ratio of each germplasm in the total mixture. All of the mixturePercentage values 
    > in this array should sum to equal 100.


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `amount` (number)

* Changed property `createdDate` (string -> string)

* Changed property `lastUpdated` (string -> string)

* Changed property `locationDbId` (string)

* Changed property `locationName` (string)

* Changed property `programDbId` (string)

* Changed property `programName` (string)

* Changed property `seedLotDescription` (string)

* Changed property `seedLotName` (string)

* Changed property `sourceCollection` (string)

* Changed property `storageLocation` (string)

* Changed property `units` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `contentMixture` (array)
            > The mixture of germplasm present in the seed lot.
            > <br/>
            > If this seed lot only contains a single germplasm, the response should contain the name 
            > and DbId of that germplasm with a mixturePercentage value of 100
            > <br/>
            > If the seed lot contains a mixture of different germplasm, the response should contain 
            > the name and DbId every germplasm present. The mixturePercentage field should contain 
            > the ratio of each germplasm in the total mixture. All of the mixturePercentage values 
            > in this array should sum to equal 100.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `seedLotDbId` (string)
            > Unique DbId for the Seed Lot


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `amount` (number)

        * Changed property `createdDate` (string -> string)

        * Changed property `lastUpdated` (string -> string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

        * Changed property `seedLotDescription` (string)

        * Changed property `seedLotName` (string)

        * Changed property `sourceCollection` (string)

        * Changed property `storageLocation` (string)

        * Changed property `units` (string)

##### `GET` /traits

> Get a filtered list of Trait


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `traitDbId` in `query`
> The unique identifier for a trait.


Changed: `observationVariableDbId` in `query`
> The unique identifier for an observation variable.


Changed: `ontologyDbId` in `query`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
>   Use `GET /ontologies` to find the list of available ontologies on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `alternativeAbbreviations` (array)
                > A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `ontologyReference` (object)

            * Deleted property `synonyms` (array)
                > Other trait names


            * Deleted property `traitDbId` (string)
                > The ID which uniquely identifies a trait


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attribute` (string)

            * Changed property `attributePUI` (string)

            * Changed property `entity` (string)

            * Changed property `entityPUI` (string)

            * Changed property `mainAbbreviation` (string)

            * Changed property `status` (string)

            * Changed property `traitClass` (string)

            * Changed property `traitDescription` (string)

            * Changed property `traitName` (string)

            * Changed property `traitPUI` (string)

##### `POST` /traits

> Create new Trait


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `alternativeAbbreviations` (array)
                > A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `ontologyReference` (object)

            * Deleted property `synonyms` (array)
                > Other trait names


            * Deleted property `traitDbId` (string)
                > The ID which uniquely identifies a trait


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `attribute` (string)

            * Changed property `attributePUI` (string)

            * Changed property `entity` (string)

            * Changed property `entityPUI` (string)

            * Changed property `mainAbbreviation` (string)

            * Changed property `status` (string)

            * Changed property `traitClass` (string)

            * Changed property `traitDescription` (string)

            * Changed property `traitName` (string)

            * Changed property `traitPUI` (string)

##### `GET` /traits/{traitDbId}


###### Parameters:

Deleted: `traitDbId` in `path`
> Id of the trait to retrieve details of.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `alternativeAbbreviations` (array)
            > A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `ontologyReference` (object)

        * Deleted property `synonyms` (array)
            > Other trait names


        * Deleted property `traitDbId` (string)
            > The ID which uniquely identifies a trait


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attribute` (string)

        * Changed property `attributePUI` (string)

        * Changed property `entity` (string)

        * Changed property `entityPUI` (string)

        * Changed property `mainAbbreviation` (string)

        * Changed property `status` (string)

        * Changed property `traitClass` (string)

        * Changed property `traitDescription` (string)

        * Changed property `traitName` (string)

        * Changed property `traitPUI` (string)

##### `PUT` /traits/{traitDbId}

> Update the details for an existing Trait


###### Parameters:

Deleted: `traitDbId` in `path`
> Id of the trait to retrieve details of.


###### Request:

Changed content type : `application/json`

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `alternativeAbbreviations` (array)
            > A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `ontologyReference` (object)

        * Deleted property `synonyms` (array)
            > Other trait names


        * Deleted property `traitDbId` (string)
            > The ID which uniquely identifies a trait


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `attribute` (string)

        * Changed property `attributePUI` (string)

        * Changed property `entity` (string)

        * Changed property `entityPUI` (string)

        * Changed property `mainAbbreviation` (string)

        * Changed property `status` (string)

        * Changed property `traitClass` (string)

        * Changed property `traitDescription` (string)

        * Changed property `traitName` (string)

        * Changed property `traitPUI` (string)

##### `GET` /variables

> Get a filtered list of ObservationVariable


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `studyDbId` in `query`
> **Deprecated in v2.1** Please use `studyDbIds`. Github issue number #483 
> <br>The unique ID of a studies to filter on


Added: `dataType` in `query`
> List of scale data types to filter search results


Added: `traitAttribute` in `query`
> A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"


Added: `traitAttributePUI` in `query`
> The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI
> <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"


Added: `traitEntity` in `query`
> A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"


Added: `traitEntityPUI` in `query`
> The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI
> <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"


Changed: `observationVariableDbId` in `query`
> The DbIds of Variables to search for


Changed: `observationVariableName` in `query`
> The names of Variables to search for


Changed: `observationVariablePUI` in `query`
> The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI


Changed: `traitClass` in `query`
> List of trait classes to filter search results


Changed: `methodDbId` in `query`
> List of methods to filter search results


Changed: `scaleDbId` in `query`
> The unique identifier for a Scale


Changed: `scaleName` in `query`
> Name of the scale
> <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable


Changed: `traitDbId` in `query`
> The unique identifier for a Trait


Changed: `traitName` in `query`
> The human readable name of a trait
> <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation


Changed: `ontologyDbId` in `query`
> List of ontology IDs to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `observationVariableDbId` (string)
                > Variable unique identifier
                > 
                > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `observationVariablePUI` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `POST` /variables

> Create new ObservationVariable


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            New required properties:
            - `methodName`
            - `scaleDbId`
            - `scaleName`
            - `traitName`

            New optional properties:
            - `method`
            - `scale`
            - `trait`

            * Added property `methodDbId` (string)

            * Added property `methodName` (string)

            * Added property `methodPUI` (string)

            * Added property `ontologyReferenceDbId` (string)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Added property `traitDbId` (string)

            * Added property `traitName` (string)

            * Added property `traitPUI` (string)

            * Deleted property `contextOfUse` (array)
                > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `method` (object)

            * Deleted property `observationVariableDbId` (string)
                > Variable unique identifier
                > 
                > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scale` (object)

            * Deleted property `synonyms` (array)
                > Other variable names


            * Deleted property `trait` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `defaultValue` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `growthStage` (string)

            * Changed property `institution` (string)

            * Changed property `language` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `observationVariablePUI` (string)

            * Changed property `scientist` (string)

            * Changed property `status` (string)

            * Changed property `submissionTimestamp` (string -> string)

##### `GET` /variables/{observationVariableDbId}

> Get the details of a specific ObservationVariable


###### Parameters:

Deleted: `observationVariableDbId` in `path`
> string id of the variable


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        New optional properties:
        - `method`
        - `scale`
        - `trait`

        * Added property `methodDbId` (string)

        * Added property `methodName` (string)

        * Added property `methodPUI` (string)

        * Added property `ontologyReferenceDbId` (string)

        * Added property `scaleDbId` (string)

        * Added property `scaleName` (string)

        * Added property `scalePUI` (string)

        * Added property `traitDbId` (string)

        * Added property `traitName` (string)

        * Added property `traitPUI` (string)

        * Deleted property `contextOfUse` (array)
            > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `method` (object)

        * Deleted property `observationVariableDbId` (string)
            > Variable unique identifier
            > 
            > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


        * Deleted property `ontologyReference` (object)

        * Deleted property `scale` (object)

        * Deleted property `synonyms` (array)
            > Other variable names


        * Deleted property `trait` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `defaultValue` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `growthStage` (string)

        * Changed property `institution` (string)

        * Changed property `language` (string)

        * Changed property `observationVariableName` (string)

        * Changed property `observationVariablePUI` (string)

        * Changed property `scientist` (string)

        * Changed property `status` (string)

        * Changed property `submissionTimestamp` (string -> string)

##### `PUT` /variables/{observationVariableDbId}

> Update the details for an existing ObservationVariable


###### Parameters:

Deleted: `observationVariableDbId` in `path`
> string id of the variable


###### Request:

Changed content type : `application/json`

New required properties:
- `methodName`
- `observationVariableDbId`
- `observationVariableDbId`
- `scaleDbId`
- `scaleName`
- `traitName`

New optional properties:
- `method`
- `scale`
- `trait`

* Added property `methodDbId` (string)

* Added property `methodName` (string)

* Added property `methodPUI` (string)

* Added property `observationVariableDbId` (string)

* Added property `ontologyReferenceDbId` (string)

* Added property `scaleDbId` (string)

* Added property `scaleName` (string)

* Added property `scalePUI` (string)

* Added property `traitDbId` (string)

* Added property `traitName` (string)

* Added property `traitPUI` (string)

* Deleted property `contextOfUse` (array)
    > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `method` (object)

* Deleted property `ontologyReference` (object)

* Deleted property `scale` (object)

* Deleted property `synonyms` (array)
    > Other variable names


* Deleted property `trait` (object)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `commonCropName` (string)

* Changed property `defaultValue` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `growthStage` (string)

* Changed property `institution` (string)

* Changed property `language` (string)

* Changed property `observationVariableName` (string)

* Changed property `observationVariablePUI` (string)

* Changed property `scientist` (string)

* Changed property `status` (string)

* Changed property `submissionTimestamp` (string -> string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        New required properties:
        - `methodName`
        - `scaleDbId`
        - `scaleName`
        - `traitName`

        New optional properties:
        - `method`
        - `scale`
        - `trait`

        * Added property `methodDbId` (string)

        * Added property `methodName` (string)

        * Added property `methodPUI` (string)

        * Added property `ontologyReferenceDbId` (string)

        * Added property `scaleDbId` (string)

        * Added property `scaleName` (string)

        * Added property `scalePUI` (string)

        * Added property `traitDbId` (string)

        * Added property `traitName` (string)

        * Added property `traitPUI` (string)

        * Deleted property `contextOfUse` (array)
            > Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `method` (object)

        * Deleted property `observationVariableDbId` (string)
            > Variable unique identifier
            > 
            > MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.


        * Deleted property `ontologyReference` (object)

        * Deleted property `scale` (object)

        * Deleted property `synonyms` (array)
            > Other variable names


        * Deleted property `trait` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `defaultValue` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `growthStage` (string)

        * Changed property `institution` (string)

        * Changed property `language` (string)

        * Changed property `observationVariableName` (string)

        * Changed property `observationVariablePUI` (string)

        * Changed property `scientist` (string)

        * Changed property `status` (string)

        * Changed property `submissionTimestamp` (string -> string)

##### `GET` /variants

> Get a filtered list of Variant


###### Parameters:

Added: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Added: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyDbId` in `query`
> List of study identifiers to search for


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `callSetDbId` in `query`
> **Deprecated in v2.1** Parameter unnecessary. Github issue number #474 
> <br/>Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.


Added: `end` in `query`
> The end of the window (0-based, exclusive) for which overlapping variants should be returned.


Added: `referenceDbId` in `query`
> The unique identifier representing a genotype `Reference`


Added: `start` in `query`
> The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variants`


Changed: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets`


Changed: `referenceDbId` in `query`
> **Deprecated in v2.1** Please use `referenceDbIds`. Github issue number #472
> <br/>Only return variants on this reference.


Changed: `referenceSetDbId` in `query`
> The unique identifier representing a genotype `ReferenceSet`


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `variantSetName` (string)

            * Deleted property `alternateBases` (array)
                > The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `alternate_bases` (array)
                > **Deprecated in v2.1** Please use `alternateBases`. Github issue number #549
                > <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `ciend` (array)
                > Similar to "cipos", but for the variant's end position (which is derived from start + svlen).


            * Deleted property `cipos` (array)
                > In the case of structural variants, start and end of the variant may not
                > be known with an exact base position. "cipos" provides an interval with
                > high confidence for the start position. The interval is provided by 0 or
                > 2 signed integers which are added to the start position.
                > Based on the use in VCF v4.2


            * Deleted property `externalReferences` (object)

            * Deleted property `filtersFailed` (array)
                > Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.


            * Deleted property `variantNames` (array)
                > A human readable name associated with a `Variant`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `created` (string -> string)

            * Changed property `end` (integer -> integer)

            * Changed property `filtersApplied` (boolean -> boolean)

            * Changed property `filtersPassed` (boolean -> boolean)

            * Changed property `referenceBases` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `start` (integer -> integer)

            * Changed property `svlen` (integer -> integer)

            * Changed property `updated` (string -> string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (array -> string)

            * Changed property `variantType` (string)

##### `GET` /variants/{variantDbId}

> Get the details of a specific Variant


###### Parameters:

Deleted: `variantDbId` in `path`
> The ID which uniquely identifies a `Variant`


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `variantSetName` (string)

        * Deleted property `alternateBases` (array)
            > The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


        * Deleted property `alternate_bases` (array)
            > **Deprecated in v2.1** Please use `alternateBases`. Github issue number #549
            > <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


        * Deleted property `ciend` (array)
            > Similar to "cipos", but for the variant's end position (which is derived from start + svlen).


        * Deleted property `cipos` (array)
            > In the case of structural variants, start and end of the variant may not
            > be known with an exact base position. "cipos" provides an interval with
            > high confidence for the start position. The interval is provided by 0 or
            > 2 signed integers which are added to the start position.
            > Based on the use in VCF v4.2


        * Deleted property `externalReferences` (object)

        * Deleted property `filtersFailed` (array)
            > Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.


        * Deleted property `variantNames` (array)
            > A human readable name associated with a `Variant`


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `created` (string -> string)

        * Changed property `end` (integer -> integer)

        * Changed property `filtersApplied` (boolean -> boolean)

        * Changed property `filtersPassed` (boolean -> boolean)

        * Changed property `referenceBases` (string)

        * Changed property `referenceDbId` (string)

        * Changed property `referenceName` (string)

        * Changed property `referenceSetDbId` (string)

        * Changed property `referenceSetName` (string)

        * Changed property `start` (integer -> integer)

        * Changed property `svlen` (integer -> integer)

        * Changed property `updated` (string -> string)

        * Changed property `variantDbId` (string)

        * Changed property `variantSetDbId` (array -> string)

        * Changed property `variantType` (string)

##### `GET` /variants/{variantDbId}/calls

> Get a filtered list of Call


###### Parameters:

Added: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Added: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variant` within the given database server


Added: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Added: `expandHomozygote` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `variantDbId` in `path`
> The ID which uniquely identifies a `Variant`


Deleted: `expandHomozygotes` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `unknownString` in `query`
> The string used as a representation for missing data.


Changed: `sepPhased` in `query`
> The string used as a separator for phased allele calls.


Changed: `sepUnphased` in `query`
> The string used as a separator for unphased allele calls.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /variantsets

> Get a filtered list of VariantSet


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `referenceDbId` in `query`
> The unique identifier representing a genotype Reference


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Changed: `variantSetDbId` in `query`
> The unique identifier representing a VariantSet


Changed: `variantDbId` in `query`
> The unique identifier representing a Variant


Changed: `callSetDbId` in `query`
> The unique identifier representing a CallSet


Changed: `referenceSetDbId` in `query`
> The unique identifier representing a genotype ReferenceSet


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `studyName` in `query`
> List of study names to filter search results


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `analysiDbIds` (array)

            * Added property `referenceSetName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `analysis` (array)
                > Set of Analysis descriptors for this VariantSet


            * Deleted property `availableFormats` (array)
                > When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats. 
                > <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)
                > <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.


            * Deleted property `externalReferences` (object)

            * Deleted property `metadataFields` (array)
                > The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet. 
                > <br> When possible, these field names and abbreviations should follow the VCF standard


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetCount` (integer -> integer)

            * Changed property `referenceSetDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `variantCount` (integer -> integer)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /variantsets/{variantSetDbId}

> Get the details of a specific VariantSet


###### Parameters:

Deleted: `variantSetDbId` in `path`
> The ID of the `Variant` to be retrieved.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `analysiDbIds` (array)

        * Added property `referenceSetName` (string)

        * Added property `studyName` (string)

        * Added property `studyPUI` (string)

        * Deleted property `analysis` (array)
            > Set of Analysis descriptors for this VariantSet


        * Deleted property `availableFormats` (array)
            > When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats. 
            > <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)
            > <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.


        * Deleted property `externalReferences` (object)

        * Deleted property `metadataFields` (array)
            > The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet. 
            > <br> When possible, these field names and abbreviations should follow the VCF standard


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `callSetCount` (integer -> integer)

        * Changed property `referenceSetDbId` (string)

        * Changed property `studyDbId` (string)

        * Changed property `variantCount` (integer -> integer)

        * Changed property `variantSetDbId` (string)

        * Changed property `variantSetName` (string)

##### `GET` /variantsets/{variantSetDbId}/calls

> Get a filtered list of Call


###### Parameters:

Added: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Added: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variant` within the given database server


Added: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Added: `expandHomozygote` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `variantSetDbId` in `path`
> The ID of the `VariantSet` to be retrieved.


Deleted: `expandHomozygotes` in `query`
> Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `unknownString` in `query`
> The string used as a representation for missing data.


Changed: `sepPhased` in `query`
> The string used as a separator for phased allele calls.


Changed: `sepUnphased` in `query`
> The string used as a separator for unphased allele calls.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Deleted property `expandHomozygotes` (boolean)
            > Should homozygotes be expanded (true) or collapsed into a single occurrence (false)


        * Deleted property `sepPhased` (string)
            > The string used as a separator for phased allele calls.


        * Deleted property `sepUnphased` (string)
            > The string used as a separator for unphased allele calls.


        * Deleted property `unknownString` (string)
            > The string used as a representation for missing data.


        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `genotype` (object)

            * Deleted property `genotypeMetadata` (array)
                > Genotype Metadata are additional layers of metadata associated with each genotype.


            * Deleted property `genotype_likelihood` (array)
                > **Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491             
                > <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.


            * Deleted property `variantName` (string)
                > The name of the variant this call belongs to.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `genotypeValue` (string)

            * Changed property `phaseSet` (string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (string)

            * Changed property `variantSetName` (string)

##### `GET` /variantsets/{variantSetDbId}/callsets

> Get a filtered list of CallSet


###### Parameters:

Added: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Added: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyDbId` in `query`
> List of study identifiers to search for


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `sampleDbId` in `query`
> A list of IDs which uniquely identify `Samples` within the given database server


Added: `sampleName` in `query`
> A list of human readable names associated with `Samples`


Added: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets` within the given database server


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Added: `externalReferenceId` in `query`
> An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Added: `externalReferenceSource` in `query`
> An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)


Deleted: `variantSetDbId` in `path`
> The ID of the `VariantSet` to be retrieved.


Changed: `callSetDbId` in `query`
> A list of IDs which uniquely identify `CallSets` within the given database server


Changed: `callSetName` in `query`
> A list of human readable names associated with `CallSets`


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sampleName` (string)

            * Added property `samplePUI` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `callSetDbId` (string)

            * Changed property `callSetName` (string)

            * Changed property `created` (string -> string)

            * Changed property `sampleDbId` (string)

            * Changed property `studyDbId` (string)

            * Changed property `updated` (string -> string)

            * Changed property `variantSetDbIds` (array)

##### `GET` /variantsets/{variantSetDbId}/variants

> Get a filtered list of Variant


###### Parameters:

Added: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Added: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyDbId` in `query`
> List of study identifiers to search for


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `callSetDbId` in `query`
> **Deprecated in v2.1** Parameter unnecessary. Github issue number #474 
> <br/>Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.


Added: `end` in `query`
> The end of the window (0-based, exclusive) for which overlapping variants should be returned.


Added: `referenceDbId` in `query`
> **Deprecated in v2.1** Please use `referenceDbIds`. Github issue number #472
> <br/>Only return variants on this reference.


Added: `referenceDbId` in `query`
> The unique identifier representing a genotype `Reference`


Added: `referenceSetDbId` in `query`
> The unique identifier representing a genotype `ReferenceSet`


Added: `start` in `query`
> The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).


Added: `variantSetDbId` in `query`
> A list of IDs which uniquely identify `VariantSets`


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Added: `externalReferenceId` in `query`
> An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Added: `externalReferenceSource` in `query`
> An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)


Deleted: `variantSetDbId` in `path`
> The ID of the `VariantSet` to be retrieved.


Deleted: `pageToken` in `query`
> **Deprecated in v2.1** Please use `page`. Github issue number #451 
> <br> Used to request a specific page of data to be returned.
> <br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.


Changed: `variantDbId` in `query`
> A list of IDs which uniquely identify `Variants`


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `variantSetName` (string)

            * Deleted property `alternateBases` (array)
                > The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `alternate_bases` (array)
                > **Deprecated in v2.1** Please use `alternateBases`. Github issue number #549
                > <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.


            * Deleted property `ciend` (array)
                > Similar to "cipos", but for the variant's end position (which is derived from start + svlen).


            * Deleted property `cipos` (array)
                > In the case of structural variants, start and end of the variant may not
                > be known with an exact base position. "cipos" provides an interval with
                > high confidence for the start position. The interval is provided by 0 or
                > 2 signed integers which are added to the start position.
                > Based on the use in VCF v4.2


            * Deleted property `externalReferences` (object)

            * Deleted property `filtersFailed` (array)
                > Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.


            * Deleted property `variantNames` (array)
                > A human readable name associated with a `Variant`


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `created` (string -> string)

            * Changed property `end` (integer -> integer)

            * Changed property `filtersApplied` (boolean -> boolean)

            * Changed property `filtersPassed` (boolean -> boolean)

            * Changed property `referenceBases` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `start` (integer -> integer)

            * Changed property `svlen` (integer -> integer)

            * Changed property `updated` (string -> string)

            * Changed property `variantDbId` (string)

            * Changed property `variantSetDbId` (array -> string)

            * Changed property `variantType` (string)

##### `GET` /crosses

> Get a filtered list of Cross


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `crossAttributes` (array)
                > Set of custom attributes associated with a cross


            * Deleted property `crossDbId` (string)
                > the unique identifier for a cross


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `pollinationEvents` (array)
                > The list of pollination events that occurred for this cross


            * Deleted property `pollinationTimeStamp` (string)
                > **Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265 
                > <br>The timestamp when the pollination took place


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossName` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                    * Property `accessionNumber` (string)

                    * Property `acquisitionDate` (string)

                    * Property `additionalInfo` (object)
                        > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                    * Property `biologicalStatusOfAccessionCode` (string)
                        > MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 
                        > 
                        > 100) Wild 
                        > 110) Natural 
                        > 120) Semi-natural/wild 
                        > 130) Semi-natural/sown 
                        > 200) Weedy 
                        > 300) Traditional cultivar/landrace 
                        > 400) Breeding/research material 
                        > 410) Breeders line 
                        > 411) Synthetic population 
                        > 412) Hybrid 
                        > 413) Founder stock/base population 
                        > 414) Inbred line (parent of hybrid cultivar) 
                        > 415) Segregating population 
                        > 416) Clonal selection 
                        > 420) Genetic stock 
                        > 421) Mutant (e.g. induced/insertion mutants, tilling populations) 
                        > 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 
                        > 423) Other genetic stocks (e.g. mapping populations) 
                        > 500) Advanced or improved cultivar (conventional breeding methods) 
                        > 600) GMO (by genetic engineering) 
                        > 999) Other (Elaborate in REMARKS field)


                        Enum values:

                        * `100`
                        * `110`
                        * `120`
                        * `130`
                        * `200`
                        * `300`
                        * `400`
                        * `410`
                        * `411`
                        * `412`
                        * `413`
                        * `414`
                        * `415`
                        * `416`
                        * `420`
                        * `421`
                        * `422`
                        * `423`
                        * `500`
                        * `600`
                        * `999`
                    * Property `biologicalStatusOfAccessionDescription` (string)

                    * Property `breedingMethodDbId` (string)

                    * Property `breedingMethodName` (string)

                    * Property `collection` (string)

                    * Property `commonCropName` (string)

                    * Property `countryOfOriginCode` (string)

                    * Property `defaultDisplayName` (string)

                    * Property `documentationURL` (string)

                    * Property `genus` (string)

                    * Property `germplasmName` (string)

                    * Property `germplasmPUI` (string)

                    * Property `germplasmPreprocessing` (string)

                    * Property `instituteCode` (string)

                    * Property `instituteName` (string)

                    * Property `pedigree` (string)

                    * Property `sampleDbIds` (array)

                    * Property `seedSource` (string)

                    * Property `seedSourceDescription` (string)

                    * Property `species` (string)

                    * Property `speciesAuthority` (string)

                    * Property `subtaxa` (string)

                    * Property `subtaxaAuthority` (string)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `PUT` /crosses

> Update the details for an existing Cross


###### Request:

Changed content type : `application/json`

New required properties:
- `crossDbId`
- `crossDbId`

* Added property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


* Added property `crossDbId` (string)

* Added property `crossName` (string)

* Added property `crossType` (string)
    > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


    Enum values:

    * `BIPARENTAL`
    * `SELF`
    * `OPEN_POLLINATED`
    * `BULK`
    * `BULK_SELFED`
    * `BULK_OPEN_POLLINATED`
    * `DOUBLE_HAPLOID`
* Added property `crossingProjectDbId` (string)

* Added property `crossingProjectName` (string)

* Added property `parent1` (object)

    * Property `germplasm` (object)

    * Property `observationUnitDbId` (string)

    * Property `observationUnitName` (string)

    * Property `observationUnitPUI` (string)

    * Property `parentType` (string)
        > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


        Enum values:

        * `MALE`
        * `FEMALE`
        * `SELF`
        * `POPULATION`
        * `CLONAL`
* Added property `parent2` (object)

* Added property `plannedCrossDbId` (string)

* Added property `plannedCrossName` (string)

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `crossAttributes` (array)
                > Set of custom attributes associated with a cross


            * Deleted property `crossDbId` (string)
                > the unique identifier for a cross


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `pollinationEvents` (array)
                > The list of pollination events that occurred for this cross


            * Deleted property `pollinationTimeStamp` (string)
                > **Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265 
                > <br>The timestamp when the pollination took place


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossName` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `POST` /crosses

> Create new Cross


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `crossAttributes` (array)
                > Set of custom attributes associated with a cross


            * Deleted property `crossDbId` (string)
                > the unique identifier for a cross


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `pollinationEvents` (array)
                > The list of pollination events that occurred for this cross


            * Deleted property `pollinationTimeStamp` (string)
                > **Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265 
                > <br>The timestamp when the pollination took place


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossName` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `GET` /plannedcrosses

> Get a filtered list of PlannedCross


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `status` (string)
                > The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').


            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `PUT` /plannedcrosses

> Update the details for an existing PlannedCross


###### Request:

Changed content type : `application/json`

New required properties:
- `plannedCrossDbId`

* Added property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


* Added property `crossType` (string)
    > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


* Added property `crossingProjectDbId` (string)

* Added property `crossingProjectName` (string)

* Added property `parent1` (object)

* Added property `parent2` (object)

* Added property `plannedCrossDbId` (string)

* Added property `plannedCrossName` (string)

* Added property `status` (string)
    > The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').


    Enum values:

    * `TODO`
    * `DONE`
    * `SKIPPED`
###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `status` (string)
                > The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').


            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `POST` /plannedcrosses

> Create new PlannedCross


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `crossType` (string)
                > The type of cross make. Accepted values for this field are 'BIPARENTAL', 'SELF', 'OPEN_POLLINATED', 'BULK',  'BULK_SELFED',  'BULK_OPEN_POLLINATED' and 'DOUBLE_HAPLOID'.


            * Changed property `crossingProjectDbId` (string)

            * Changed property `crossingProjectName` (string)

            * Changed property `plannedCrossDbId` (string)

            * Changed property `plannedCrossName` (string)

            * Changed property `status` (string)
                > The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').


            * Changed property `parent1` (object)

                * Added property `germplasm` (object)

                * Added property `observationUnitPUI` (string)

                * Deleted property `germplasmDbId` (string)
                    > the unique identifier for a germplasm


                * Deleted property `germplasmName` (string)
                    > the human readable name for a germplasm


                * Changed property `observationUnitDbId` (string)

                * Changed property `observationUnitName` (string)

                * Changed property `parentType` (string)
                    > The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'. \n\nIn a pedigree record, the 'parentType' describes each parent of a particular germplasm. \n\nIn a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny. \nFor example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers \nto the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C.\nIn this way, A could be a male parent to B, but a female parent to C.


                    Added enum value:

                    * `CLONAL`
##### `GET` /references

> Get a filtered list of Reference


###### Parameters:

Added: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Changed: `referenceDbId` in `query`
> A list of IDs which uniquely identify `References` within the given database server


Changed: `referenceSetDbId` in `query`
> A list of IDs which uniquely identify `ReferenceSets` within the given database server


Changed: `accession` in `query`
> If specified, return the references for which the `accession` matches this string (case-sensitive, exact match).


Changed: `isDerived` in `query`
> A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.


Changed: `minLength` in `query`
> The minimum length of this `References` sequence.


Changed: `maxLength` in `query`
> The minimum length of this `References` sequence.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `length` (integer -> integer)

            * Changed property `md5checksum` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceDivergence` (number -> number)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `GET` /references/{referenceDbId}

> Get the details of a specific Reference


###### Parameters:

Deleted: `referenceDbId` in `path`
> The ID of the `Reference` to be retrieved.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `sourceGermplasmDbIds` (array)

        * Added property `variantDbIds` (array)

        * Deleted property `externalReferences` (object)

        * Deleted property `sourceAccessions` (array)
            > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.


        * Deleted property `sourceGermplasm` (array)
            > All known corresponding Germplasm


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `isDerived` (boolean -> boolean)

        * Changed property `length` (integer -> integer)

        * Changed property `md5checksum` (string)

        * Changed property `referenceDbId` (string)

        * Changed property `referenceName` (string)

        * Changed property `referenceSetDbId` (string)

        * Changed property `referenceSetName` (string)

        * Changed property `sourceDivergence` (number -> number)

        * Changed property `sourceURI` (string)

        * Changed property `species` (object)

            * Changed property `term` (string)

            * Changed property `termURI` (string)

##### `GET` /referencesets

> Get a filtered list of ReferenceSet


###### Parameters:

Added: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `externalReferenceID` in `query`
> **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 
> <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)


Changed: `referenceSetDbId` in `query`
> The `ReferenceSets` to search.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `referenceDbId` (string)

            * Added property `referenceName` (string)

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Added property `variantSetDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `referenceSetDbId` (string)
                > The unique identifier for a ReferenceSet


            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `assemblyPUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `description` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `md5checksum` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `GET` /referencesets/{referenceSetDbId}

> Get the details of a specific ReferenceSet


###### Parameters:

Deleted: `referenceSetDbId` in `path`
> The ID of the `ReferenceSet` to be retrieved.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

New response : **400 Bad Request**
New response : **401 Unauthorized**
New response : **403 Forbidden**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `referenceDbId` (string)

        * Added property `referenceName` (string)

        * Added property `sourceGermplasmDbIds` (array)

        * Added property `variantDbIds` (array)

        * Added property `variantSetDbIds` (array)

        * Deleted property `externalReferences` (object)

        * Deleted property `referenceSetDbId` (string)
            > The unique identifier for a ReferenceSet


        * Deleted property `sourceAccessions` (array)
            > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.


        * Deleted property `sourceGermplasm` (array)
            > All known corresponding Germplasm


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `assemblyPUI` (string)

        * Changed property `commonCropName` (string)

        * Changed property `description` (string)

        * Changed property `isDerived` (boolean -> boolean)

        * Changed property `md5checksum` (string)

        * Changed property `referenceSetName` (string)

        * Changed property `sourceURI` (string)

        * Changed property `species` (object)

            * Changed property `term` (string)

            * Changed property `termURI` (string)

##### `GET` /scales

> Get a filtered list of Scale


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `scaleDbId` in `query`
> The unique identifier for a scale.


Changed: `observationVariableDbId` in `query`
> The unique identifier for an observation variable.


Changed: `ontologyDbId` in `query`
> The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology 
> 
>   Use `GET /ontologies` to find the list of available ontologies on a server.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scaleDbId` (string)
                > Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dataType` (string)
                > <p>Class of the scale, entries can be</p>
                > <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p>
                > <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p>
                > <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p>
                > <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p>
                > <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p>
                > <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p>
                > <p>"Text" - A free text is used to express the trait.</p>


            * Changed property `decimalPlaces` (integer -> integer)

            * Changed property `scaleName` (string)

            * Changed property `scalePUI` (string)

            * Changed property `units` (string)

            * Changed property `validValues` (object)

                * Added property `scaleDbId` (string)

                * Added property `scaleName` (string)

                * Added property `scalePUI` (string)

                * Deleted property `categories` (array)
                    > List of possible values with optional labels


                * Deleted property `max` (integer)
                    > **Deprecated in v2.1** Please use `maximumValue`. Github issue number #450 
                    > <br>Maximum value for numerical scales. Typically used for data capture control and QC.


                * Deleted property `min` (integer)
                    > **Deprecated in v2.1** Please use `minimumValue`. Github issue number #450 
                    > <br>Minimum value for numerical scales. Typically used for data capture control and QC.


                * Changed property `maximumValue` (string)

                * Changed property `minimumValue` (string)

##### `POST` /scales

> Create new Scale


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `ontologyReferenceDbId` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `ontologyReference` (object)

            * Deleted property `scaleDbId` (string)
                > Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `dataType` (string)
                > <p>Class of the scale, entries can be</p>
                > <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p>
                > <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p>
                > <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p>
                > <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p>
                > <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p>
                > <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p>
                > <p>"Text" - A free text is used to express the trait.</p>


            * Changed property `decimalPlaces` (integer -> integer)

            * Changed property `scaleName` (string)

            * Changed property `scalePUI` (string)

            * Changed property `units` (string)

            * Changed property `validValues` (object)

                * Added property `scaleDbId` (string)

                * Added property `scaleName` (string)

                * Added property `scalePUI` (string)

                * Deleted property `categories` (array)
                    > List of possible values with optional labels


                * Deleted property `max` (integer)
                    > **Deprecated in v2.1** Please use `maximumValue`. Github issue number #450 
                    > <br>Maximum value for numerical scales. Typically used for data capture control and QC.


                * Deleted property `min` (integer)
                    > **Deprecated in v2.1** Please use `minimumValue`. Github issue number #450 
                    > <br>Minimum value for numerical scales. Typically used for data capture control and QC.


                * Changed property `maximumValue` (string)

                * Changed property `minimumValue` (string)

##### `GET` /scales/{scaleDbId}


###### Parameters:

Deleted: `scaleDbId` in `path`
> Id of the scale to retrieve details of.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `ontologyReference` (object)

        * Deleted property `scaleDbId` (string)
            > Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `dataType` (string)
            > <p>Class of the scale, entries can be</p>
            > <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p>
            > <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p>
            > <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p>
            > <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p>
            > <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p>
            > <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p>
            > <p>"Text" - A free text is used to express the trait.</p>


        * Changed property `decimalPlaces` (integer -> integer)

        * Changed property `scaleName` (string)

        * Changed property `scalePUI` (string)

        * Changed property `units` (string)

        * Changed property `validValues` (object)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Deleted property `categories` (array)
                > List of possible values with optional labels


            * Deleted property `max` (integer)
                > **Deprecated in v2.1** Please use `maximumValue`. Github issue number #450 
                > <br>Maximum value for numerical scales. Typically used for data capture control and QC.


            * Deleted property `min` (integer)
                > **Deprecated in v2.1** Please use `minimumValue`. Github issue number #450 
                > <br>Minimum value for numerical scales. Typically used for data capture control and QC.


            * Changed property `maximumValue` (string)

            * Changed property `minimumValue` (string)

##### `PUT` /scales/{scaleDbId}

> Update the details for an existing Scale


###### Parameters:

Deleted: `scaleDbId` in `path`
> Id of the scale to retrieve details of.


###### Request:

Changed content type : `application/json`

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `ontologyReferenceDbId` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `ontologyReference` (object)

        * Deleted property `scaleDbId` (string)
            > Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `dataType` (string)
            > <p>Class of the scale, entries can be</p>
            > <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p>
            > <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p>
            > <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p>
            > <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p>
            > <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p>
            > <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p>
            > <p>"Text" - A free text is used to express the trait.</p>


        * Changed property `decimalPlaces` (integer -> integer)

        * Changed property `scaleName` (string)

        * Changed property `scalePUI` (string)

        * Changed property `units` (string)

        * Changed property `validValues` (object)

            * Added property `scaleDbId` (string)

            * Added property `scaleName` (string)

            * Added property `scalePUI` (string)

            * Deleted property `categories` (array)
                > List of possible values with optional labels


            * Deleted property `max` (integer)
                > **Deprecated in v2.1** Please use `maximumValue`. Github issue number #450 
                > <br>Maximum value for numerical scales. Typically used for data capture control and QC.


            * Deleted property `min` (integer)
                > **Deprecated in v2.1** Please use `minimumValue`. Github issue number #450 
                > <br>Minimum value for numerical scales. Typically used for data capture control and QC.


            * Changed property `maximumValue` (string)

            * Changed property `minimumValue` (string)

##### `POST` /search/references

> Submit a search request for `Reference`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `length` (integer -> integer)

            * Changed property `md5checksum` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceDivergence` (number -> number)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `GET` /search/references/{searchResultsDbId}

> Submit a search request for `Reference`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/reference/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `length` (integer -> integer)

            * Changed property `md5checksum` (string)

            * Changed property `referenceDbId` (string)

            * Changed property `referenceName` (string)

            * Changed property `referenceSetDbId` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceDivergence` (number -> number)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `POST` /search/referencesets

> Submit a search request for `ReferenceSet`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `referenceDbId` (string)

            * Added property `referenceName` (string)

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Added property `variantSetDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `referenceSetDbId` (string)
                > The unique identifier for a ReferenceSet


            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `assemblyPUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `description` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `md5checksum` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `GET` /search/referencesets/{searchResultsDbId}

> Submit a search request for `ReferenceSet`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/referenceSet/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `referenceDbId` (string)

            * Added property `referenceName` (string)

            * Added property `sourceGermplasmDbIds` (array)

            * Added property `variantDbIds` (array)

            * Added property `variantSetDbIds` (array)

            * Deleted property `externalReferences` (object)

            * Deleted property `referenceSetDbId` (string)
                > The unique identifier for a ReferenceSet


            * Deleted property `sourceAccessions` (array)
                > All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.


            * Deleted property `sourceGermplasm` (array)
                > All known corresponding Germplasm


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `assemblyPUI` (string)

            * Changed property `commonCropName` (string)

            * Changed property `description` (string)

            * Changed property `isDerived` (boolean -> boolean)

            * Changed property `md5checksum` (string)

            * Changed property `referenceSetName` (string)

            * Changed property `sourceURI` (string)

            * Changed property `species` (object)

                * Changed property `term` (string)

                * Changed property `termURI` (string)

##### `POST` /search/studies

> Submit a search request for `Study`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `contactDbIds` (array)

            * Added property `environmentParameterDbIds` (array)

            * Added property `lastUpdateDbId` (string)

            * Added property `trialPUI` (string)

            * Deleted property `contacts` (array)
                > List of contact entities associated with this study


            * Deleted property `dataLinks` (array)
                > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


            * Deleted property `environmentParameters` (array)
                > Environmental parameters that were kept constant throughout the study and did not change between observation units.
                > 
                > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `lastUpdate` (object)

            * Deleted property `observationLevels` (array)
                > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


            * Deleted property `seasons` (array)
                > List of seasons over which this study was performed.


            * Deleted property `studyDbId` (string)
                > The ID which uniquely identifies a study within the given database server
                > 
                > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `culturalPractices` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `license` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitsDescription` (string)

            * Changed property `observationVariableDbIds` (array)

            * Changed property `startDate` (string -> string)

            * Changed property `studyCode` (string)

            * Changed property `studyDescription` (string)

            * Changed property `studyName` (string)

            * Changed property `studyPUI` (string)

            * Changed property `studyType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

            * Changed property `experimentalDesign` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

            * Changed property `growthFacility` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

##### `GET` /search/studies/{searchResultsDbId}

> Submit a search request for `Study`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/study/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `contactDbIds` (array)

            * Added property `environmentParameterDbIds` (array)

            * Added property `lastUpdateDbId` (string)

            * Added property `trialPUI` (string)

            * Deleted property `contacts` (array)
                > List of contact entities associated with this study


            * Deleted property `dataLinks` (array)
                > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


            * Deleted property `environmentParameters` (array)
                > Environmental parameters that were kept constant throughout the study and did not change between observation units.
                > 
                > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `lastUpdate` (object)

            * Deleted property `observationLevels` (array)
                > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


            * Deleted property `seasons` (array)
                > List of seasons over which this study was performed.


            * Deleted property `studyDbId` (string)
                > The ID which uniquely identifies a study within the given database server
                > 
                > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `culturalPractices` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `license` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitsDescription` (string)

            * Changed property `observationVariableDbIds` (array)

            * Changed property `startDate` (string -> string)

            * Changed property `studyCode` (string)

            * Changed property `studyDescription` (string)

            * Changed property `studyName` (string)

            * Changed property `studyPUI` (string)

            * Changed property `studyType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

            * Changed property `experimentalDesign` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

            * Changed property `growthFacility` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

##### `POST` /search/trials

> Submit a search request for `Trial`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `studyDbIds` (array)

            * Deleted property `datasetAuthorships` (array)
                > License and citation information for the data in this trial


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `publications` (array)
                > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


            * Deleted property `trialDbId` (string)
                > The ID which uniquely identifies a trial
                > 
                > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `startDate` (string -> string)

            * Changed property `trialDescription` (string)

            * Changed property `trialName` (string)

            * Changed property `trialPUI` (string)

            * Changed property `contacts` (array)

                Changed items (object):

                * Changed property `contactDbId` (string)

                * Changed property `email` (string)

                * Changed property `instituteName` (string)

                * Changed property `name` (string)

                * Changed property `orcid` (string)

                * Changed property `type` (string)

##### `GET` /search/trials/{searchResultsDbId}

> Submit a search request for `Trial`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/trial/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `studyDbIds` (array)

            * Deleted property `datasetAuthorships` (array)
                > License and citation information for the data in this trial


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `publications` (array)
                > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


            * Deleted property `trialDbId` (string)
                > The ID which uniquely identifies a trial
                > 
                > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `startDate` (string -> string)

            * Changed property `trialDescription` (string)

            * Changed property `trialName` (string)

            * Changed property `trialPUI` (string)

            * Changed property `contacts` (array)

                Changed items (object):

                * Changed property `contactDbId` (string)

                * Changed property `email` (string)

                * Changed property `instituteName` (string)

                * Changed property `name` (string)

                * Changed property `orcid` (string)

                * Changed property `type` (string)

##### `GET` /studies

> Get a filtered list of Study


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `locationName` in `query`
> A human readable names to search for


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `observationVariableName` in `query`
> The names of Variables to search for


Added: `observationVariablePUI` in `query`
> The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI


Added: `actife` in `query`
> A flag to indicate if a Study is currently active and ongoing


Deleted: `active` in `query`
> A flag to indicate if a Study is currently active and ongoing


Deleted: `sortBy` in `query`
> Name of the field to sort by.


Deleted: `sortOrder` in `query`
> Sort order direction. Ascending/Descending.


Changed: `studyType` in `query`
> The type of study being performed. ex. "Yield Trial", etc


Changed: `locationDbId` in `query`
> The location ids to search for


Changed: `seasonDbId` in `query`
> The ID which uniquely identifies a season


Changed: `studyCode` in `query`
> A short human readable code for a study


Changed: `studyPUI` in `query`
> Permanent unique identifier associated with study data. For example, a URI or DOI


Changed: `observationVariableDbId` in `query`
> The DbIds of Variables to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `studyName` in `query`
> List of study names to filter search results


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `contactDbIds` (array)

            * Added property `environmentParameterDbIds` (array)

            * Added property `lastUpdateDbId` (string)

            * Added property `trialPUI` (string)

            * Deleted property `contacts` (array)
                > List of contact entities associated with this study


            * Deleted property `dataLinks` (array)
                > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


            * Deleted property `environmentParameters` (array)
                > Environmental parameters that were kept constant throughout the study and did not change between observation units.
                > 
                > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `lastUpdate` (object)

            * Deleted property `observationLevels` (array)
                > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


            * Deleted property `seasons` (array)
                > List of seasons over which this study was performed.


            * Deleted property `studyDbId` (string)
                > The ID which uniquely identifies a study within the given database server
                > 
                > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `culturalPractices` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `license` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitsDescription` (string)

            * Changed property `observationVariableDbIds` (array)

            * Changed property `startDate` (string -> string)

            * Changed property `studyCode` (string)

            * Changed property `studyDescription` (string)

            * Changed property `studyName` (string)

            * Changed property `studyPUI` (string)

            * Changed property `studyType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

            * Changed property `experimentalDesign` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

            * Changed property `growthFacility` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

##### `POST` /studies

> Create new Study


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `contactDbIds` (array)

            * Added property `environmentParameterDbIds` (array)

            * Added property `lastUpdateDbId` (string)

            * Added property `trialPUI` (string)

            * Deleted property `contacts` (array)
                > List of contact entities associated with this study


            * Deleted property `dataLinks` (array)
                > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


            * Deleted property `environmentParameters` (array)
                > Environmental parameters that were kept constant throughout the study and did not change between observation units.
                > 
                > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `lastUpdate` (object)

            * Deleted property `observationLevels` (array)
                > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


            * Deleted property `seasons` (array)
                > List of seasons over which this study was performed.


            * Deleted property `studyDbId` (string)
                > The ID which uniquely identifies a study within the given database server
                > 
                > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `culturalPractices` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `license` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `observationUnitsDescription` (string)

            * Changed property `observationVariableDbIds` (array)

            * Changed property `startDate` (string -> string)

            * Changed property `studyCode` (string)

            * Changed property `studyDescription` (string)

            * Changed property `studyName` (string)

            * Changed property `studyPUI` (string)

            * Changed property `studyType` (string)

            * Changed property `trialDbId` (string)

            * Changed property `trialName` (string)

            * Changed property `experimentalDesign` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

            * Changed property `growthFacility` (object)

                * Added property `studyDbId` (string)

                * Added property `studyName` (string)

                * Added property `studyPUI` (string)

                * Changed property `PUI` (string)

                * Changed property `description` (string)

##### `GET` /studies/{studyDbId}

> Get the details of a specific Study


###### Parameters:

Deleted: `studyDbId` in `path`
> Identifier of the study. Usually a number, could be alphanumeric.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `contactDbIds` (array)

        * Added property `environmentParameterDbIds` (array)

        * Added property `lastUpdateDbId` (string)

        * Added property `trialPUI` (string)

        * Deleted property `contacts` (array)
            > List of contact entities associated with this study


        * Deleted property `dataLinks` (array)
            > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


        * Deleted property `environmentParameters` (array)
            > Environmental parameters that were kept constant throughout the study and did not change between observation units.
            > 
            > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `lastUpdate` (object)

        * Deleted property `observationLevels` (array)
            > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


        * Deleted property `seasons` (array)
            > List of seasons over which this study was performed.


        * Deleted property `studyDbId` (string)
            > The ID which uniquely identifies a study within the given database server
            > 
            > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


        * Changed property `active` (boolean)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `culturalPractices` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `endDate` (string -> string)

        * Changed property `license` (string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `observationUnitsDescription` (string)

        * Changed property `observationVariableDbIds` (array)

        * Changed property `startDate` (string -> string)

        * Changed property `studyCode` (string)

        * Changed property `studyDescription` (string)

        * Changed property `studyName` (string)

        * Changed property `studyPUI` (string)

        * Changed property `studyType` (string)

        * Changed property `trialDbId` (string)

        * Changed property `trialName` (string)

        * Changed property `experimentalDesign` (object)

            * Added property `studyDbId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Changed property `PUI` (string)

            * Changed property `description` (string)

        * Changed property `growthFacility` (object)

            * Added property `studyDbId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Changed property `PUI` (string)

            * Changed property `description` (string)

##### `PUT` /studies/{studyDbId}

> Update the details for an existing Study


###### Parameters:

Deleted: `studyDbId` in `path`
> Identifier of the study. Usually a number, could be alphanumeric.


###### Request:

Changed content type : `application/json`

New required properties:
- `studyDbId`
- `studyDbId`

* Added property `contactDbIds` (array)

* Added property `environmentParameterDbIds` (array)

* Added property `lastUpdateDbId` (string)

* Added property `studyDbId` (string)

* Added property `trialPUI` (string)

* Deleted property `contacts` (array)
    > List of contact entities associated with this study


* Deleted property `dataLinks` (array)
    > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


* Deleted property `environmentParameters` (array)
    > Environmental parameters that were kept constant throughout the study and did not change between observation units.
    > 
    > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `lastUpdate` (object)

* Deleted property `observationLevels` (array)
    > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


* Deleted property `seasons` (array)
    > List of seasons over which this study was performed.


* Changed property `active` (boolean)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `commonCropName` (string)

* Changed property `culturalPractices` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `endDate` (string -> string)

* Changed property `license` (string)

* Changed property `locationDbId` (string)

* Changed property `locationName` (string)

* Changed property `observationUnitsDescription` (string)

* Changed property `observationVariableDbIds` (array)

* Changed property `startDate` (string -> string)

* Changed property `studyCode` (string)

* Changed property `studyDescription` (string)

* Changed property `studyName` (string)

* Changed property `studyPUI` (string)

* Changed property `studyType` (string)

* Changed property `trialDbId` (string)

* Changed property `trialName` (string)

* Changed property `experimentalDesign` (object)

    * Added property `studyDbId` (string)

    * Added property `studyName` (string)

    * Added property `studyPUI` (string)

    * Changed property `PUI` (string)

    * Changed property `description` (string)

* Changed property `growthFacility` (object)

    * Added property `studyDbId` (string)

    * Added property `studyName` (string)

    * Added property `studyPUI` (string)

    * Changed property `PUI` (string)

    * Changed property `description` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `contactDbIds` (array)

        * Added property `environmentParameterDbIds` (array)

        * Added property `lastUpdateDbId` (string)

        * Added property `trialPUI` (string)

        * Deleted property `contacts` (array)
            > List of contact entities associated with this study


        * Deleted property `dataLinks` (array)
            > List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.


        * Deleted property `environmentParameters` (array)
            > Environmental parameters that were kept constant throughout the study and did not change between observation units.
            > 
            > MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `lastUpdate` (object)

        * Deleted property `observationLevels` (array)
            > Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).


        * Deleted property `seasons` (array)
            > List of seasons over which this study was performed.


        * Deleted property `studyDbId` (string)
            > The ID which uniquely identifies a study within the given database server
            > 
            > MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.


        * Changed property `active` (boolean)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `culturalPractices` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `endDate` (string -> string)

        * Changed property `license` (string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `observationUnitsDescription` (string)

        * Changed property `observationVariableDbIds` (array)

        * Changed property `startDate` (string -> string)

        * Changed property `studyCode` (string)

        * Changed property `studyDescription` (string)

        * Changed property `studyName` (string)

        * Changed property `studyPUI` (string)

        * Changed property `studyType` (string)

        * Changed property `trialDbId` (string)

        * Changed property `trialName` (string)

        * Changed property `experimentalDesign` (object)

            * Added property `studyDbId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Changed property `PUI` (string)

            * Changed property `description` (string)

        * Changed property `growthFacility` (object)

            * Added property `studyDbId` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Changed property `PUI` (string)

            * Changed property `description` (string)

##### `GET` /trials

> Get a filtered list of Trial


###### Parameters:

Added: `locationName` in `query`
> A human readable names to search for


Added: `observationVariableDbId` in `query`
> The DbIds of Variables to search for


Added: `observationVariableName` in `query`
> The names of Variables to search for


Added: `observationVariablePUI` in `query`
> The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `actife` in `query`
> A flag to indicate if a Trial is currently active and ongoing


Deleted: `active` in `query`
> A flag to indicate if a Trial is currently active and ongoing


Deleted: `sortBy` in `query`
> Sort order. Name of the field to sort by.


Deleted: `sortOrder` in `query`
> Sort order direction: asc/desc


Changed: `contactDbId` in `query`
> List of contact entities associated with this trial


Changed: `locationDbId` in `query`
> The location ids to search for


Changed: `searchDateRangeStart` in `query`
> The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.
> 
> Return a Trial entity if any of the following cases are true
> 
> - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null 
> 
> - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`
> 
> - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null
> 
> - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`


Changed: `searchDateRangeEnd` in `query`
> The end of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.
> 
> Return a Trial entity if any of the following cases are true
> 
> - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null 
> 
> - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`
> 
> - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null
> 
> - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`


Changed: `trialPUI` in `query`
> A permanent identifier for a trial. Could be DOI or other URI formatted identifier.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `trialName` in `query`
> The human readable name of a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `studyDbIds` (array)

            * Deleted property `datasetAuthorships` (array)
                > License and citation information for the data in this trial


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `publications` (array)
                > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


            * Deleted property `trialDbId` (string)
                > The ID which uniquely identifies a trial
                > 
                > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `startDate` (string -> string)

            * Changed property `trialDescription` (string)

            * Changed property `trialName` (string)

            * Changed property `trialPUI` (string)

            * Changed property `contacts` (array)

                Changed items (object):

                * Changed property `contactDbId` (string)

                * Changed property `email` (string)

                * Changed property `instituteName` (string)

                * Changed property `name` (string)

                * Changed property `orcid` (string)

                * Changed property `type` (string)

##### `POST` /trials

> Create new Trial


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `studyDbIds` (array)

            * Deleted property `datasetAuthorships` (array)
                > License and citation information for the data in this trial


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `publications` (array)
                > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


            * Deleted property `trialDbId` (string)
                > The ID which uniquely identifies a trial
                > 
                > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


            * Changed property `active` (boolean)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `commonCropName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `endDate` (string -> string)

            * Changed property `programDbId` (string)

            * Changed property `programName` (string)

            * Changed property `startDate` (string -> string)

            * Changed property `trialDescription` (string)

            * Changed property `trialName` (string)

            * Changed property `trialPUI` (string)

            * Changed property `contacts` (array)

                Changed items (object):

                * Changed property `contactDbId` (string)

                * Changed property `email` (string)

                * Changed property `instituteName` (string)

                * Changed property `name` (string)

                * Changed property `orcid` (string)

                * Changed property `type` (string)

##### `GET` /trials/{trialDbId}


###### Parameters:

Deleted: `trialDbId` in `path`
> The internal trialDbId


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `studyDbIds` (array)

        * Deleted property `datasetAuthorships` (array)
            > License and citation information for the data in this trial


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `publications` (array)
            > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


        * Deleted property `trialDbId` (string)
            > The ID which uniquely identifies a trial
            > 
            > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


        * Changed property `active` (boolean)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `endDate` (string -> string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

        * Changed property `startDate` (string -> string)

        * Changed property `trialDescription` (string)

        * Changed property `trialName` (string)

        * Changed property `trialPUI` (string)

        * Changed property `contacts` (array)

            Changed items (object):

            * Changed property `contactDbId` (string)

            * Changed property `email` (string)

            * Changed property `instituteName` (string)

            * Changed property `name` (string)

            * Changed property `orcid` (string)

            * Changed property `type` (string)

##### `PUT` /trials/{trialDbId}

> Update the details for an existing Trial


###### Parameters:

Deleted: `trialDbId` in `path`
> The internal trialDbId


###### Request:

Changed content type : `application/json`

New required properties:
- `trialDbId`
- `trialDbId`

* Added property `studyDbIds` (array)

* Added property `trialDbId` (string)

* Deleted property `datasetAuthorships` (array)
    > License and citation information for the data in this trial


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `publications` (array)
    > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


* Changed property `active` (boolean)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `commonCropName` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `endDate` (string -> string)

* Changed property `programDbId` (string)

* Changed property `programName` (string)

* Changed property `startDate` (string -> string)

* Changed property `trialDescription` (string)

* Changed property `trialName` (string)

* Changed property `trialPUI` (string)

* Changed property `contacts` (array)

    Changed items (object):

    * Changed property `contactDbId` (string)

    * Changed property `email` (string)

    * Changed property `instituteName` (string)

    * Changed property `name` (string)

    * Changed property `orcid` (string)

    * Changed property `type` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `studyDbIds` (array)

        * Deleted property `datasetAuthorships` (array)
            > License and citation information for the data in this trial


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `publications` (array)
            > MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.


        * Deleted property `trialDbId` (string)
            > The ID which uniquely identifies a trial
            > 
            > MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.


        * Changed property `active` (boolean)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `commonCropName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `endDate` (string -> string)

        * Changed property `programDbId` (string)

        * Changed property `programName` (string)

        * Changed property `startDate` (string -> string)

        * Changed property `trialDescription` (string)

        * Changed property `trialName` (string)

        * Changed property `trialPUI` (string)

        * Changed property `contacts` (array)

            Changed items (object):

            * Changed property `contactDbId` (string)

            * Changed property `email` (string)

            * Changed property `instituteName` (string)

            * Changed property `name` (string)

            * Changed property `orcid` (string)

            * Changed property `type` (string)

##### `GET` /images

> Get a filtered list of Image


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `imageFileName` in `query`
> Image file names to search for.


Added: `imageFileSizeMax` in `query`
> A maximum image file size to search for.


Added: `imageFileSizeMin` in `query`
> A minimum image file size to search for.


Added: `imageHeightMax` in `query`
> A maximum image height to search for.


Added: `imageHeightMin` in `query`
> A minimum image height to search for.


Added: `imageLocation` in `query`

Added: `imageTimeStampRangeEnd` in `query`
> The latest timestamp to search for.


Added: `imageTimeStampRangeStart` in `query`
> The earliest timestamp to search for.


Added: `imageWidthMax` in `query`
> A maximum image width to search for.


Added: `imageWidthMin` in `query`
> A minimum image width to search for.


Added: `mimeType` in `query`
> A set of image file types to search for.


Changed: `imageDbId` in `query`
> A list of image Ids to search for


Changed: `imageName` in `query`
> Human readable names to search for.


Changed: `observationUnitDbId` in `query`
> A set of observation unit identifiers to search for.


Changed: `observationDbId` in `query`
> A list of observation Ids this image is associated with to search for


Changed: `descriptiveOntologyTerm` in `query`
> A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Deleted property `descriptiveOntologyTerms` (array)
                > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `imageDbId` (string)
                > The unique identifier of an image


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `imageFileName` (string)

            * Changed property `imageFileSize` (integer -> integer)

            * Changed property `imageHeight` (integer -> integer)

            * Changed property `imageName` (string)

            * Changed property `imageTimeStamp` (string -> string)

            * Changed property `imageURL` (string)

            * Changed property `imageWidth` (integer -> integer)

            * Changed property `mimeType` (string)

            * Changed property `observationDbIds` (array)

            * Changed property `observationUnitDbId` (string)

            * Changed property `imageLocation` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `POST` /images

> Create new Image


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Deleted property `descriptiveOntologyTerms` (array)
                > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `imageDbId` (string)
                > The unique identifier of an image


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `imageFileName` (string)

            * Changed property `imageFileSize` (integer -> integer)

            * Changed property `imageHeight` (integer -> integer)

            * Changed property `imageName` (string)

            * Changed property `imageTimeStamp` (string -> string)

            * Changed property `imageURL` (string)

            * Changed property `imageWidth` (integer -> integer)

            * Changed property `mimeType` (string)

            * Changed property `observationDbIds` (array)

            * Changed property `observationUnitDbId` (string)

            * Changed property `imageLocation` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /images/{imageDbId}

> Get the details of a specific Image


###### Parameters:

Deleted: `imageDbId` in `path`
> The unique identifier for a image


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `observationUnitName` (string)

        * Added property `observationUnitPUI` (string)

        * Deleted property `descriptiveOntologyTerms` (array)
            > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `imageDbId` (string)
            > The unique identifier of an image


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `copyright` (string)

        * Changed property `description` (string)

        * Changed property `imageFileName` (string)

        * Changed property `imageFileSize` (integer -> integer)

        * Changed property `imageHeight` (integer -> integer)

        * Changed property `imageName` (string)

        * Changed property `imageTimeStamp` (string -> string)

        * Changed property `imageURL` (string)

        * Changed property `imageWidth` (integer -> integer)

        * Changed property `mimeType` (string)

        * Changed property `observationDbIds` (array)

        * Changed property `observationUnitDbId` (string)

        * Changed property `imageLocation` (object)
            > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
            > 
            > Copied from RFC 7946 Section 3.1.1
            > 
            > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
            > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


            * Changed property `type` (string)

            * Changed property `geometry` (object -> object)

##### `PUT` /images/{imageDbId}

> Update the details for an existing Image


###### Parameters:

Deleted: `imageDbId` in `path`
> The unique identifier for a image


###### Request:

Changed content type : `application/json`

New required properties:
- `imageDbId`
- `imageDbId`

* Added property `imageDbId` (string)

* Added property `observationUnitName` (string)

* Added property `observationUnitPUI` (string)

* Deleted property `descriptiveOntologyTerms` (array)
    > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `copyright` (string)

* Changed property `description` (string)

* Changed property `imageFileName` (string)

* Changed property `imageFileSize` (integer -> integer)

* Changed property `imageHeight` (integer -> integer)

* Changed property `imageName` (string)

* Changed property `imageTimeStamp` (string -> string)

* Changed property `imageURL` (string)

* Changed property `imageWidth` (integer -> integer)

* Changed property `mimeType` (string)

* Changed property `observationDbIds` (array)

* Changed property `observationUnitDbId` (string)

* Changed property `imageLocation` (object)
    > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
    > 
    > Copied from RFC 7946 Section 3.1.1
    > 
    > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
    > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


    * Changed property `type` (string)

    * Changed property `geometry` (object -> object)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `observationUnitName` (string)

        * Added property `observationUnitPUI` (string)

        * Deleted property `descriptiveOntologyTerms` (array)
            > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `imageDbId` (string)
            > The unique identifier of an image


        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `copyright` (string)

        * Changed property `description` (string)

        * Changed property `imageFileName` (string)

        * Changed property `imageFileSize` (integer -> integer)

        * Changed property `imageHeight` (integer -> integer)

        * Changed property `imageName` (string)

        * Changed property `imageTimeStamp` (string -> string)

        * Changed property `imageURL` (string)

        * Changed property `imageWidth` (integer -> integer)

        * Changed property `mimeType` (string)

        * Changed property `observationDbIds` (array)

        * Changed property `observationUnitDbId` (string)

        * Changed property `imageLocation` (object)
            > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
            > 
            > Copied from RFC 7946 Section 3.1.1
            > 
            > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
            > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


            * Changed property `type` (string)

            * Changed property `geometry` (object -> object)

##### `GET` /locations

> Get a filtered list of Location


###### Parameters:

Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `abbreviation` in `query`
> A list of shortened human readable names for a set of Locations


Added: `altitudeMin` in `query`
> The minimum altitude to search for


Added: `altitudeMax` in `query`
> The maximum altitude to search for


Added: `countryCode` in `query`
> [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec


Added: `countryName` in `query`
> The full name of the country to search for


Added: `coordinate` in `query`

Added: `instituteAddress` in `query`
> The street address of the institute to search for


Added: `instituteName` in `query`
> The name of the institute to search for


Changed: `locationType` in `query`
> The type of location this represents (ex. Breeding Location, Storage Location, etc)


Changed: `locationDbId` in `query`
> The location ids to search for


Changed: `locationName` in `query`
> A human readable names to search for


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `childLocationDbIds` (array)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `parentLocationDbId` (string)
                > The unique identifier for a Location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Deleted property `parentLocationName` (string)
                > A human readable name for a location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `coordinateDescription` (string)

            * Changed property `coordinateUncertainty` (string)

            * Changed property `countryCode` (string)

            * Changed property `countryName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `environmentType` (string)

            * Changed property `exposure` (string)

            * Changed property `instituteAddress` (string)

            * Changed property `instituteName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `locationType` (string)

            * Changed property `siteStatus` (string)

            * Changed property `slope` (string)

            * Changed property `topography` (string)

            * Changed property `coordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `POST` /locations

> Create new Location


###### Request:

Changed content type : `application/json`

###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `childLocationDbIds` (array)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `parentLocationDbId` (string)
                > The unique identifier for a Location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Deleted property `parentLocationName` (string)
                > A human readable name for a location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `coordinateDescription` (string)

            * Changed property `coordinateUncertainty` (string)

            * Changed property `countryCode` (string)

            * Changed property `countryName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `environmentType` (string)

            * Changed property `exposure` (string)

            * Changed property `instituteAddress` (string)

            * Changed property `instituteName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `locationType` (string)

            * Changed property `siteStatus` (string)

            * Changed property `slope` (string)

            * Changed property `topography` (string)

            * Changed property `coordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /locations/{locationDbId}


###### Parameters:

Deleted: `locationDbId` in `path`
> The internal DB id for a location


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `childLocationDbIds` (array)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `parentLocationDbId` (string)
            > The unique identifier for a Location
            > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
            > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


        * Deleted property `parentLocationName` (string)
            > A human readable name for a location
            > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
            > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


        * Changed property `abbreviation` (string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `coordinateDescription` (string)

        * Changed property `coordinateUncertainty` (string)

        * Changed property `countryCode` (string)

        * Changed property `countryName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `environmentType` (string)

        * Changed property `exposure` (string)

        * Changed property `instituteAddress` (string)

        * Changed property `instituteName` (string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `locationType` (string)

        * Changed property `siteStatus` (string)

        * Changed property `slope` (string)

        * Changed property `topography` (string)

        * Changed property `coordinates` (object)
            > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
            > 
            > Copied from RFC 7946 Section 3.1.1
            > 
            > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
            > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


            * Changed property `type` (string)

            * Changed property `geometry` (object -> object)

##### `PUT` /locations/{locationDbId}


###### Parameters:

Deleted: `locationDbId` in `path`
> The internal DB id for a location


###### Request:

Changed content type : `application/json`

New required properties:
- `locationDbId`
- `locationDbId`

* Added property `childLocationDbIds` (array)

* Added property `locationDbId` (string)

* Deleted property `externalReferences` (array)
    > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


* Deleted property `parentLocationDbId` (string)
    > The unique identifier for a Location
    > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
    > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


* Deleted property `parentLocationName` (string)
    > A human readable name for a location
    > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
    > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


* Changed property `abbreviation` (string)

* Changed property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


    * Added property `additionalProperties` (string)

* Changed property `coordinateDescription` (string)

* Changed property `coordinateUncertainty` (string)

* Changed property `countryCode` (string)

* Changed property `countryName` (string)

* Changed property `documentationURL` (string -> string)

* Changed property `environmentType` (string)

* Changed property `exposure` (string)

* Changed property `instituteAddress` (string)

* Changed property `instituteName` (string)

* Changed property `locationName` (string)

* Changed property `locationType` (string)

* Changed property `siteStatus` (string)

* Changed property `slope` (string)

* Changed property `topography` (string)

* Changed property `coordinates` (object)
    > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
    > 
    > Copied from RFC 7946 Section 3.1.1
    > 
    > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
    > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


    * Changed property `type` (string)

    * Changed property `geometry` (object -> object)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `childLocationDbIds` (array)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `parentLocationDbId` (string)
            > The unique identifier for a Location
            > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
            > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


        * Deleted property `parentLocationName` (string)
            > A human readable name for a location
            > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
            > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


        * Changed property `abbreviation` (string)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `coordinateDescription` (string)

        * Changed property `coordinateUncertainty` (string)

        * Changed property `countryCode` (string)

        * Changed property `countryName` (string)

        * Changed property `documentationURL` (string -> string)

        * Changed property `environmentType` (string)

        * Changed property `exposure` (string)

        * Changed property `instituteAddress` (string)

        * Changed property `instituteName` (string)

        * Changed property `locationDbId` (string)

        * Changed property `locationName` (string)

        * Changed property `locationType` (string)

        * Changed property `siteStatus` (string)

        * Changed property `slope` (string)

        * Changed property `topography` (string)

        * Changed property `coordinates` (object)
            > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
            > 
            > Copied from RFC 7946 Section 3.1.1
            > 
            > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
            > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


            * Changed property `type` (string)

            * Changed property `geometry` (object -> object)

##### `GET` /observations

> Get a filtered list of Observation


###### Parameters:

Added: `germplasmName` in `query`
> List of human readable names to identify germplasm to search for


Added: `locationName` in `query`
> A human readable names to search for


Added: `observationVariableName` in `query`
> The names of Variables to search for


Added: `observationVariablePUI` in `query`
> The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI


Added: `programName` in `query`
> Use this parameter to only return results associated with the given program names. Program names are not required to be unique.
> 
> Use `GET /programs` to find the list of available programs on a server.


Added: `studyName` in `query`
> List of study names to filter search results


Added: `trialName` in `query`
> The human readable name of a trial to search for


Added: `observationLevel` in `query`
> Searches for values in ObservationUnit->observationUnitPosition->observationLevel


Added: `observationLevelRelationship` in `query`
> Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships


Deleted: `observationUnitLevelName` in `query`
> The Observation Unit Level. Returns only the observation unit of the specified Level. 
> <br/>References ObservationUnit->observationUnitPosition->observationLevel->levelName 
> <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelOrder` in `query`
> The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. 
> References ObservationUnit->observationUnitPosition->observationLevel->levelOrder 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelCode` in `query`
> The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` 
> or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipName` in `query`
> The Observation Unit Level Relationship is a connection that this observation unit has to another level of the hierarchy. 
> <br/>For example, if you have several observation units at a 'plot' level, they might all share a relationship to the same 'field' level.  
> <br/>Use this parameter to identify groups of observation units that share a relationship level. 
> <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipOrder` in `query`
> The Observation Unit Level Order Number. 
> <br/>Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipCode` in `query`
> The Observation Unit Level Code. 
> <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Deleted: `observationUnitLevelRelationshipDbId` in `query`
> The observationUnitDbId associated with a particular level and code.
> <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->observationUnitDbId 
> <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.


Changed: `observationDbId` in `query`
> The unique id of an Observation


Changed: `observationUnitDbId` in `query`
> The unique id of an Observation Unit


Changed: `observationVariableDbId` in `query`
> The DbIds of Variables to search for


Changed: `locationDbId` in `query`
> The location ids to search for


Changed: `observationTimeStampRangeStart` in `query`
> Timestamp range start


Changed: `observationTimeStampRangeEnd` in `query`
> Timestamp range end


Changed: `commonCropName` in `query`
> The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.
> 
> Use this parameter to only return results associated with the given crops. 
> 
> Use `GET /commoncropnames` to find the list of available crops on a server.


Changed: `programDbId` in `query`
> A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
> 
> Use this parameter to only return results associated with the given programs. 
> 
> Use `GET /programs` to find the list of available programs on a server.


Changed: `trialDbId` in `query`
> The ID which uniquely identifies a trial to search for


Changed: `studyDbId` in `query`
> List of study identifiers to search for


Changed: `germplasmDbId` in `query`
> List of IDs which uniquely identify germplasm to search for


###### Return Type:

Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `observationVariablePUI` (string)

            * Added property `seasonDbId` (string)

            * Added property `seasonName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationDbId` (string)
                > The ID which uniquely identifies an observation


            * Deleted property `season` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `collector` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `observationTimeStamp` (string -> string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationVariableDbId` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `uploadedBy` (string)

            * Changed property `value` (string)

            * Changed property `geoCoordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `PUT` /observations

> Update the details for an existing Observation


###### Request:

Changed content type : `application/json`

New required properties:
- `observationDbId`
- `observationDbId`

* Added property `additionalInfo` (object)
    > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


* Added property `collector` (string)

* Added property `geoCoordinates` (object)
    > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
    > 
    > Copied from RFC 7946 Section 3.1.1
    > 
    > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
    > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


    * Property `geometry` (object)

        One of:

            * Property `coordinates` (array)

                Items (number):

            * Property `type` (string)

            * Property `coordinates` (array)

                Items (array):

                Items (array):

            * Property `type` (string)

    * Property `type` (string)

* Added property `germplasmDbId` (string)

* Added property `germplasmName` (string)

* Added property `germplasmPUI` (string)

* Added property `observationDbId` (string)

* Added property `observationTimeStamp` (string)

* Added property `observationUnitDbId` (string)

* Added property `observationUnitName` (string)

* Added property `observationUnitPUI` (string)

* Added property `observationVariableDbId` (string)

* Added property `observationVariableName` (string)

* Added property `observationVariablePUI` (string)

* Added property `seasonDbId` (string)

* Added property `seasonName` (string)

* Added property `studyDbId` (string)

* Added property `studyName` (string)

* Added property `studyPUI` (string)

* Added property `uploadedBy` (string)

* Added property `value` (string)

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `observationVariablePUI` (string)

            * Added property `seasonDbId` (string)

            * Added property `seasonName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationDbId` (string)
                > The ID which uniquely identifies an observation


            * Deleted property `season` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `collector` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `observationTimeStamp` (string -> string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationVariableDbId` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `uploadedBy` (string)

            * Changed property `value` (string)

            * Changed property `geoCoordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `POST` /observations

> Create new Observation


###### Request:

Changed content type : `application/json`

###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `observationVariablePUI` (string)

            * Added property `seasonDbId` (string)

            * Added property `seasonName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationDbId` (string)
                > The ID which uniquely identifies an observation


            * Deleted property `season` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `collector` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `observationTimeStamp` (string -> string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationVariableDbId` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `uploadedBy` (string)

            * Changed property `value` (string)

            * Changed property `geoCoordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /observations/{observationDbId}

> Get the details of a specific Observation


###### Parameters:

Deleted: `observationDbId` in `path`
> The unique ID of an observation


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Added property `germplasmPUI` (string)

        * Added property `observationUnitPUI` (string)

        * Added property `observationVariablePUI` (string)

        * Added property `seasonDbId` (string)

        * Added property `seasonName` (string)

        * Added property `studyName` (string)

        * Added property `studyPUI` (string)

        * Deleted property `externalReferences` (array)
            > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


        * Deleted property `observationDbId` (string)
            > The ID which uniquely identifies an observation


        * Deleted property `season` (object)

        * Changed property `additionalInfo` (object)
            > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


            * Added property `additionalProperties` (string)

        * Changed property `collector` (string)

        * Changed property `germplasmDbId` (string)

        * Changed property `germplasmName` (string)

        * Changed property `observationTimeStamp` (string -> string)

        * Changed property `observationUnitDbId` (string)

        * Changed property `observationUnitName` (string)

        * Changed property `observationVariableDbId` (string)

        * Changed property `observationVariableName` (string)

        * Changed property `studyDbId` (string)

        * Changed property `uploadedBy` (string)

        * Changed property `value` (string)

        * Changed property `geoCoordinates` (object)
            > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
            > 
            > Copied from RFC 7946 Section 3.1.1
            > 
            > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
            > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


            * Changed property `type` (string)

            * Changed property `geometry` (object -> object)

##### `POST` /search/images

> Submit a search request for `Image`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Deleted property `descriptiveOntologyTerms` (array)
                > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `imageDbId` (string)
                > The unique identifier of an image


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `imageFileName` (string)

            * Changed property `imageFileSize` (integer -> integer)

            * Changed property `imageHeight` (integer -> integer)

            * Changed property `imageName` (string)

            * Changed property `imageTimeStamp` (string -> string)

            * Changed property `imageURL` (string)

            * Changed property `imageWidth` (integer -> integer)

            * Changed property `mimeType` (string)

            * Changed property `observationDbIds` (array)

            * Changed property `observationUnitDbId` (string)

            * Changed property `imageLocation` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /search/images/{searchResultsDbId}

> Submit a search request for `Image`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/image/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Deleted response : **404 Not Found**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `observationUnitName` (string)

            * Added property `observationUnitPUI` (string)

            * Deleted property `descriptiveOntologyTerms` (array)
                > A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.


            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `imageDbId` (string)
                > The unique identifier of an image


            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `copyright` (string)

            * Changed property `description` (string)

            * Changed property `imageFileName` (string)

            * Changed property `imageFileSize` (integer -> integer)

            * Changed property `imageHeight` (integer -> integer)

            * Changed property `imageName` (string)

            * Changed property `imageTimeStamp` (string -> string)

            * Changed property `imageURL` (string)

            * Changed property `imageWidth` (integer -> integer)

            * Changed property `mimeType` (string)

            * Changed property `observationDbIds` (array)

            * Changed property `observationUnitDbId` (string)

            * Changed property `imageLocation` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `POST` /search/locations

> Submit a search request for `Location`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `childLocationDbIds` (array)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `parentLocationDbId` (string)
                > The unique identifier for a Location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Deleted property `parentLocationName` (string)
                > A human readable name for a location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `coordinateDescription` (string)

            * Changed property `coordinateUncertainty` (string)

            * Changed property `countryCode` (string)

            * Changed property `countryName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `environmentType` (string)

            * Changed property `exposure` (string)

            * Changed property `instituteAddress` (string)

            * Changed property `instituteName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `locationType` (string)

            * Changed property `siteStatus` (string)

            * Changed property `slope` (string)

            * Changed property `topography` (string)

            * Changed property `coordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /search/locations/{searchResultsDbId}

> Submit a search request for `Location`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/location/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `childLocationDbIds` (array)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `parentLocationDbId` (string)
                > The unique identifier for a Location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to. 
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Deleted property `parentLocationName` (string)
                > A human readable name for a location
                > <br/> The Parent Location defines the encompassing Location that a smaller Location belongs to.  
                > For example, an Institution might have multiple Field Stations inside it and each Field Station might have multiple Fields.


            * Changed property `abbreviation` (string)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `coordinateDescription` (string)

            * Changed property `coordinateUncertainty` (string)

            * Changed property `countryCode` (string)

            * Changed property `countryName` (string)

            * Changed property `documentationURL` (string -> string)

            * Changed property `environmentType` (string)

            * Changed property `exposure` (string)

            * Changed property `instituteAddress` (string)

            * Changed property `instituteName` (string)

            * Changed property `locationDbId` (string)

            * Changed property `locationName` (string)

            * Changed property `locationType` (string)

            * Changed property `siteStatus` (string)

            * Changed property `slope` (string)

            * Changed property `topography` (string)

            * Changed property `coordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `POST` /search/observations

> Submit a search request for `Observation`


###### Parameters:

Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


###### Request:

Deleted content type : `application/json`

###### Return Type:

Changed response : **202 Accepted**
> Accepted


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `observationVariablePUI` (string)

            * Added property `seasonDbId` (string)

            * Added property `seasonName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationDbId` (string)
                > The ID which uniquely identifies an observation


            * Deleted property `season` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `collector` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `observationTimeStamp` (string -> string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationVariableDbId` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `uploadedBy` (string)

            * Changed property `value` (string)

            * Changed property `geoCoordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

##### `GET` /search/observations/{searchResultsDbId}

> Submit a search request for `Observation`<br/>
> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
> If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
> Use the corresponding `GET /search/observation/{searchResultsDbId}` to retrieve the results of the search. <br/> 
> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.


###### Parameters:

Deleted: `Accept` in `header`
> A standard HTTP request header that is used to request a specific content type (JSON, CSV, etc) which is "acceptable" to the client and should be returned by the server


Deleted: `Authorization` in `header`
> HTTP HEADER - Token used for Authorization 
> 
> <strong> Bearer {token_string} </strong>


Deleted: `searchResultsDbId` in `path`
> Unique identifier which references the search results


Deleted: `page` in `query`
> Used to request a specific page of data to be returned.
> 
> The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


Deleted: `pageSize` in `query`
> The size of the pages to be returned. Default is `1000`.


###### Return Type:

Deleted response : **202 Accepted**
Changed response : **200 OK**
> OK


* Changed content type : `application/json`

    * Changed property `metadata` (object -> object)
        > An object in the BrAPI standard response model that describes some information about the service call being performed. This includes supplementary data, status log messages, and pagination information.


    * Changed property `result` (object)

        * Changed property `data` (array)

            Changed items (object):

            * Added property `germplasmPUI` (string)

            * Added property `observationUnitPUI` (string)

            * Added property `observationVariablePUI` (string)

            * Added property `seasonDbId` (string)

            * Added property `seasonName` (string)

            * Added property `studyName` (string)

            * Added property `studyPUI` (string)

            * Deleted property `externalReferences` (array)
                > An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.


            * Deleted property `observationDbId` (string)
                > The ID which uniquely identifies an observation


            * Deleted property `season` (object)

            * Changed property `additionalInfo` (object)
                > A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.


                * Added property `additionalProperties` (string)

            * Changed property `collector` (string)

            * Changed property `germplasmDbId` (string)

            * Changed property `germplasmName` (string)

            * Changed property `observationTimeStamp` (string -> string)

            * Changed property `observationUnitDbId` (string)

            * Changed property `observationUnitName` (string)

            * Changed property `observationVariableDbId` (string)

            * Changed property `observationVariableName` (string)

            * Changed property `studyDbId` (string)

            * Changed property `uploadedBy` (string)

            * Changed property `value` (string)

            * Changed property `geoCoordinates` (object)
                > One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.
                > 
                > Copied from RFC 7946 Section 3.1.1
                > 
                > A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or
                > easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.


                * Changed property `type` (string)

                * Changed property `geometry` (object -> object)

