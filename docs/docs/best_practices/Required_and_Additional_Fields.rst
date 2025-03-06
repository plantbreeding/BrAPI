Required and Additional Fields
==============================

Required Fields and Parameters
------------------------------
From the perspective of the BrAPI Specification, most data fields are not required. Data fields and parameters that are required 
by the BrAPI specification are marked in the documentation by a red star (*) symbol, or the bolded word "Required". Generally, 
for each entity in the BrAPI specification, the entity DbId and the entity Name are the only two fields required. There are a 
exceptions to this rule, for example the "List" entity also requires a "listType" field to fully understood.

For most data fields in the BrAPI specification, required-ness should be determined by the specific use case and systems involved.
For example, a genebank system dealing with Germplasm records might maintain important "germplasmOrigin" information, and all incoming
records are required to have that field populated. However, a breeding system doesn't care about "germplasmOrigin" and doesn't
even store that metadata in any permanent storage. In that case, "germplasmOrigin" is not only optional, but not even maintained
at all and will be lost if someone assumes it is required. This is simply to illustrate that every use case and software system 
is unique, and defining too many required fields across the whole community will inevitably lead to conflicting situations. 

Additional Fields and Parameters
--------------------------------
Additional data can be added to any response, depending on the use case and systems involved. All BrAPI response objects have an 
`additionalInfo` section which is defined as a free form JSON object. This is to help organize data fields, keeping the standard
fields separate from the custom fields. 

It is HIGHLY RECOMMENDED to open a new issue on GitHub for any fields added to `additionalInfo` in production systems. In some cases,
additional metadata is only used for specific systems or specific connections. In other cases, they indicate a missing piece of the 
BrAPI specification that others in the community might also need. In still other cases, there might be a different place in the 
specification the developers are unaware of that better represents the data using the spec. 

Deprecated Fields and Parameters
--------------------------------
Deprecated endpoints and fields should be included only if the given server wants to support backwards compatibility. Deprecated 
fields can be removed from a response if there is no need to support an earlier version any more. See the section on Versioning for 
more information.


Missing Fields and Null Data
----------------------------
There are two ways to indicate "no data": give the field a value of `null` or omit the field from the JSON object entirely. In almost
all cases, these two methods should be considered equivalent by all BrAPI implementations. An empty string value (`""`) is not 
considered equivalent and should be considered as valid data. 

+----------------------------+---------------------------+----------------------------+
| NULL (no data)             | Omitted (no data)         | Empty String (data)        |
+============================+===========================+============================+
|| {                         || {                        || {                         |
|| "programDbId": "xyz123",  || "programDbId": "xyz123", || "programDbId": "xyz123",  |
|| "programName": "Program", || "programName": "Program" || "programName": "Program", |
|| "objective": null         || }                        || "objective": ""           |
|| }                         ||                          || }                         |
+----------------------------+---------------------------+----------------------------+

Considering `null` and an omitted field as equivalent works for all BrAPI Response objects and all BrAPI POST Request objects. However,
for BrAPI PUT Request objects, used to update an existing record, `null` and omitted must be handled separately. For PUT requests, an 
omitted field should be ignored, but an explicit `null` value should be accepted to over-write that data field. The omitted field tells
the server to not update that field, the `null` value tells the server to explicitly remove the previous value and replace it with "no 
data". 
