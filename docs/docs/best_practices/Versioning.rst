Versioning
==========

Major Verions
-------------
Major versions of the BrAPI spec are accompanied by broad changes to the whole specifcation. Major versions are not backward compatable with each other. 
When a new major version is built, all the deprecated fields are perminantly removed, allowing for a clean slate to start again. 
This is why it is important to indicate the major version in the URL for every BrAPI call. If a server needs to support multiple major versions of the spec,
each version will be implemented under a different base path. 

Minor Verions
-------------
Minor versions are typically smaller updates to the spec, fixing a group of smaller github issues like new search parameters, additional data fields, and mistakes not following best practice. 
Minor versions are backward compatible, so a single response can have all the data fields nessesary to support the needs of multiple minor versions. 


Deprecation
-----------
Deprecated fields, parameters, and endpoints indicate that something has been removed or replaced in a minor version update. 

