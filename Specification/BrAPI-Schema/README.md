## JSON Specification 

The BrAPI Specification defined as a JSON Schema. The schema is 
defined in individual files per Entity in separate models.
Some files contain more than one definition where the entity has
Value Types that are used only by entity. 

[BrAPI-Common](./BrAPI-Common) contains definitions that are used the
accose the four main.

[Requests](./Requests) defines the query model in the form of request 
object definitions for the primary entity models. 
Shared parameters and object definition between these definitions are placed in the
[Parameters](./Requests/Parameters) and [Schemas](./Requests/Schemas) 
directories respectively.