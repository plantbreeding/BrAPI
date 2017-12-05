# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.

## Observation variable data response

`required` means the key has to be provided, but the value may be null.

Variable                       | Required | Type            | Description
------------------------------ | :------: | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
observationVariableDbId        |    Y     | string          | Variable unique identifier
name                           |    Y     | string          | Variable name (usually a short name)
ontologyDbId                   |    Y     | string          | Variable ontology unique identifier
ontologyName                   |    Y     | string          | Variable ontology name (usually a short name)
synonyms                       |          | array of string | Other variable names
contextOfUse                   |          | array of string | Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])
growthStage                    |          | string          | Growth stage at which measurement is made (examples: "flowering")
status                         |          | string          | Variable status. (examples: "recommended", "obsolete", "legacy", etc.)
xref                           |          | string          | Cross reference of the variable term to a term from an external ontology or to a database of a major system.
institution                    |          | string          | Name of institution submitting the variable
scientist                      |          | string          | Name of scientist submitting the variable.
date                           |          | string          | Date of submission of the variable (ISO 8601).
language                       |          | string          | 2 letter ISO code for the language of submission of the variable.
crop                           |          | string          | Crop name (examples: "Maize", "Wheat")
trait                          |    Y     | object          | Trait metadata
trait.traitDbId                |    Y     | string          | Trait unique identifier
trait.name                     |    Y     | string          | Trait name (usually a short name)
trait.class                    |          | string          | Trait class. (examples: "morphological trait", "phenological trait", "agronomical trait", "physiological trait", "abiotic stress trait", "biotic stress trait", "biochemical trait", "quality traits trait", "fertility trait", etc.)
trait.description              |          | string          | Trait description.
trait.synonyms                 |          | array of string | Other trait names
trait.mainAbbreviation         |          | string          | Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")
trait.alternativeAbbreviations |          | array of string | Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention. If several aternative abbreviations, separate with commas.
trait.entity                   |          | string          | A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"
trait.attribute                |          | string          | A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"
trait.status                   |          | string          | Trait status (examples: "recommended", "obsolete", "legacy", etc.)
trait.xref                     |          | string          | Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term
method                         |    Y     | object          | Method metadata
method.methodDbId              |          | string          | Method unique identifier
method.name                    |          | string          | Method name (usually a short name)
method.class                   |          | string          | Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.
method.description             |          | string          | Method description.
method.formula                 |          | string          | For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation
method.reference               |          | string          | Bibliographical reference describing the method.
scale                          |    Y     | object          | Scale metadata
scale.scaleDbId                |          | string          | Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.
scale.name                     |          | string          | Name of the scale
scale.class                    |          | string          | Class of the scale, entries can be "Numerical", "Nominal", "Ordinal", "Text", "Code", "Time", "Duration"
scale.decimalPlaces            |          | numeric         | For numerical, number of decimal places to be reported
scale.xref                     |          | string          | Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database
scale.validValues.min          |          | numeric         | Minimum value (used for data capture control) for numerical and date scales
scale.validValues.max          |          | numeric         | Maximum value (used for field data capture control).
scale.validValues.categories   |          | array of string | List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]
defaultValue                   |    Y     | string          | Variable default value. (examples: "red", "2.3", etc.)

## Ontology data response

`required` means the key has to be provided, but the value may be null.

Variable     | Required | Type   | Description
------------ | :------: | ------ | -----------------------------------------------
ontologyDbId |    Y     | string | Ontology database unique identifier
ontologyName |    Y     | string | Ontology name
authors      |          | string | Ontology's list of authors (no specific format)
version      |          | string | Ontology version (no specific format)
copyright    |          | string | Ontology copyright
licence      |          | string | Ontology licence
