Required and Additional Fields
==============================


Required Fields and Parameters
------------------------------
From the perspective of the BrAPI Specification, most data fields are not required. 

Additional Fields and Parameters
--------------------------------
Additional data can be added to any response. Most response objects have an `additionalInfo` section which is a free form JSON object. 

Deprecated Fields and Parameters
--------------------------------
Deprecated endpoints and fields should be included only if the given server wants to support backwards compatibility. 
Deprecated fields can be removed from a response if there is no need to support an earilier version any more. See the section on Versioning for more information.

